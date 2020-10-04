from typing import IO, Any, Dict, List

import yaml

from .utils import convert_to_camel_case


def load(top_class_name: str, obj: Any, class_dict: Dict[str, Any]) -> Any:
    def parse(class_name, *args, **kwargs):
        if args:
            if isinstance(args[0], dict):
                return [parse(class_name[:-1], **value) for value in args]
            return list(args)
        if kwargs:
            class_name = convert_to_camel_case(class_name, True)
            values = []
            for key, value in kwargs.items():
                if isinstance(value, dict):
                    values.append(parse(key, **value))
                elif isinstance(value, list):
                    values.append(parse(key, *value))
                else:
                    values.append(value)
            return class_dict[class_name](*values)
    return parse(top_class_name, **obj)


def load_yaml(file: IO, top_class_name: str, classes: List[Any]) -> Any:
    obj = yaml.safe_load(file)
    class_dict = {class_.__name__: class_ for class_ in classes}
    return load(top_class_name, obj, class_dict)
