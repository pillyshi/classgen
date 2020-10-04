import re


def convert_to_camel_case(string, titleCase=False) -> str:
    """
    https://oboe2uran.hatenablog.com/entry/2019/10/01/083415
    """
    if titleCase:
        return ''.join(x.title() for x in string.split('_'))
    else:
        return re.sub("_(.)", lambda m: m.group(1).upper(), string.lower())
