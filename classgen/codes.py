from typing import List, Tuple, Set, Any
from collections import namedtuple

from .utils import convert_to_camel_case


variable_template = '    {}: {}'


class_template = """
class {}(NamedTuple):
{}
"""


def get_type_string(obj) -> str:
    if isinstance(obj, list):
        type_string = str(type(obj[0])).split(' ')[1][1:-2]
        type_string = type_string.split('.')[-1]
        return f'List[{type_string}]'
    type_string = str(type(obj)).split(' ')[1][1:-2]
    return type_string.split('.')[-1]


def get_class_string(class_name: str, variables: List[Tuple[str, str]]) -> str:
    return class_template.format(
        class_name,
        '\n'.join(variable_template.format(variable, variable_type)
                  for variable, variable_type in variables)
    ).strip()


def get_class_strings_from_dict(class_name, obj) -> List[str]:
    class_names = []
    variables_list = []

    def parse(class_name, *args, **kwargs):
        nonlocal class_names
        nonlocal variables_list
        if args:
            if isinstance(args[0], dict):
                return [parse(class_name[:-1], **value) for value in args]
            return list(args)
        if kwargs:
            T = namedtuple(convert_to_camel_case(class_name, True), list(kwargs.keys()))
            values = []
            for key, value in kwargs.items():
                if isinstance(value, dict):
                    values.append(parse(key, **value))
                elif isinstance(value, list):
                    values.append(parse(key, *value))
                else:
                    values.append(value)
            class_names += [convert_to_camel_case(class_name, True)]
            variables_list += [list(zip(kwargs.keys(), map(get_type_string, values)))]
            return T(*values)
    parse(class_name, **obj)
    class_strings: List[str] = []
    already_added: Set[str] = set()
    for class_name, variables in zip(class_names, variables_list):
        class_string = get_class_string(class_name, variables)
        if class_string in already_added:
            continue
        class_strings.append(class_string)
        already_added.add(class_string)
    return class_strings


def get_class_string_from_dict(top_class_name: str, obj: Any) -> str:
    class_string = ''
    class_strings = get_class_strings_from_dict(top_class_name, obj)

    typing_modules = ['NamedTuple']
    if any('List' in class_string for class_string in class_strings):
        typing_modules.append('List')

    class_string += f'from typing import {", ".join(typing_modules)}\n'
    class_string += '\n\n'
    class_string += '\n\n\n'.join(class_strings)
    class_string += '\n\n'
    return class_string
