import re
import json
from collections import namedtuple

import yaml


def convert_to_camel_case(string, titleCase=False):
    """
    https://oboe2uran.hatenablog.com/entry/2019/10/01/083415
    """
    if titleCase:
        return ''.join(x.title() for x in string.split('_'))
    else:
        return re.sub("_(.)", lambda m: m.group(1).upper(), string.lower())


def get_object_from_dict(_class_name, *args, **kwargs):
    if args:
        if isinstance(args[0], dict):
            return [get_object_from_dict(_class_name[:-1], **value) for value in args]
        return list(args)

    if kwargs:
        T = namedtuple(convert_to_camel_case(_class_name, True), list(kwargs.keys()))
        values = []
        for key, value in kwargs.items():
            if isinstance(value, dict):
                values.append(get_object_from_dict(key, **value))
            elif isinstance(value, list):
                values.append(get_object_from_dict(key, *value))
            else:
                values.append(value)
        return T(*values)


def get_object_from_file(filename: str):
    ext = filename.split('/')[-1].split('.')[1]
    if ext == 'yaml' or ext == 'yml':
        get_object_from_yaml(filename)
    elif ext == 'json':
        get_object_from_json(filename)


def get_object_from_yaml(filename: str):
    with open(filename) as f:
        obj_dict = yaml.safe_load(f)
    obj = get_object_from_dict(obj_dict)
    return obj


def get_object_from_json(filename: str):
    with open(filename) as f:
        obj_dict = json.load(f)
    obj = get_object_from_dict(obj_dict)
    return obj
