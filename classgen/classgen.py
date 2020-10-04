import json
from tap import Tap

import yaml

from .codes import get_class_string_from_dict


class Option(Tap):
    top_class_name: str
    in_file: str
    out_file: str


def main(option: Option):
    if option.in_file.endswith('.yaml') or option.in_file.endswith('.yml'):
        with open(option.in_file) as f:
            obj = yaml.safe_load(f)
    elif option.in_file.endswith('.json'):
        with open(option.in_file) as f:
            obj = json.load(f)
    else:
        raise ValueError()
    class_string = get_class_string_from_dict(option.top_class_name, obj)
    with open(option.out_file, 'w') as f:
        print(class_string, end='', file=f)


if __name__ == "__main__":
    option = Option().parse_args()
    main(option)
