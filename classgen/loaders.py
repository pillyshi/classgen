import json
from typing import IO, Any, Dict, List, TypeVar, Type

import yaml

from .utils import convert_to_camel_case


T = TypeVar('T')


def load(top_class: Type[T], obj: Any, class_dict: Dict[str, Any]) -> T:
    def parse(class_: Type[Any], *args, **kwargs) -> Any:
        if args:
            if isinstance(args[0], dict):
                return [parse(class_, **value) for value in args]
            return list(args)
        elif kwargs:
            values = []
            for key, value in kwargs.items():
                key_camel = convert_to_camel_case(key, True)
                if isinstance(value, dict):
                    values.append(parse(class_dict[key_camel], **value))
                elif isinstance(value, list):
                    values.append(parse(class_dict[key_camel[:-1]], *value))
                else:
                    values.append(value)
            return class_(*values)
        else:
            raise ValueError()
    return parse(top_class, **obj)


def load_yaml(file: IO, top_class: Type[T], classes: List[Any]) -> T:
    obj = yaml.safe_load(file)
    class_dict = {class_.__name__: class_ for class_ in classes}
    return load(top_class, obj, class_dict)


def load_json(file: IO, top_class: Type[T], classes: List[Any]) -> T:
    obj = json.load(file)
    class_dict = {class_.__name__: class_ for class_ in classes}
    return load(top_class, obj, class_dict)
