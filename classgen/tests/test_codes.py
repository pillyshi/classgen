from classgen.codes import get_class_string, get_class_strings_from_dict, get_class_string_from_dict


def test_get_class_string():
    class_name = 'Company'
    variables = [
        ('id', 'int'),
        ('name', 'str')
    ]
    _class_string = get_class_string(class_name, variables)
    class_string = """
class Company(NamedTuple):
    id: int
    name: str
    """.strip()

    assert _class_string == class_string


def test_get_class_strings_from_dict():
    company = {
        'id': 1,
        'name': 'example corporation'
    }
    _class_strings = get_class_strings_from_dict('Company', company)
    class_strings = ["""
class Company(NamedTuple):
    id: int
    name: str
    """.strip()
    ]
    for class_string, _class_string in zip(class_strings, _class_strings):
        assert _class_string == class_string

    info = {
        'company': {
            'id': 1,
            'name': 'example corporation'
        }
    }
    _class_strings = get_class_strings_from_dict('Info', info)
    class_strings = ["""
class Company(NamedTuple):
    id: int
    name: str
    """.strip(), """
class Info(NamedTuple):
    company: Company
    """.strip()
    ]
    for class_string, _class_string in zip(class_strings, _class_strings):
        assert _class_string == class_string

    info = {
        'company': {
            'id': 1,
            'name': 'example corporation',
            'employees': [
                'tanaka',
                'yamada'
            ]
        }
    }
    _class_strings = get_class_strings_from_dict('Info', info)
    class_strings = ["""
class Company(NamedTuple):
    id: int
    name: str
    employees: List[str]
    """.strip(), """
class Info(NamedTuple):
    company: Company
    """.strip()
    ]
    for class_string, _class_string in zip(class_strings, _class_strings):
        assert _class_string == class_string

    info = {
        'company': {
            'id': 1,
            'name': 'example corporation',
            'employees': [
                {
                    'id': 1,
                    'name': 'tanaka'
                },
                {
                    'id': 2,
                    'name': 'yamada'
                }
            ]
        }
    }
    _class_strings = get_class_strings_from_dict('Info', info)
    class_strings = ["""
class Employee(NamedTuple):
    id: int
    name: str
    """.strip(), """
class Company(NamedTuple):
    id: int
    name: str
    employees: List[Employee]
    """.strip(), """
class Info(NamedTuple):
    company: Company
    """.strip()
    ]
    for class_string, _class_string in zip(class_strings, _class_strings):
        assert _class_string == class_string


def test_get_class_string_from_dict():
    info = {
        'company': {
            'id': 1,
            'name': 'example corporation',
            'employees': [
                {
                    'id': 1,
                    'name': 'tanaka'
                },
                {
                    'id': 2,
                    'name': 'yamada'
                }
            ]
        }
    }
    _class_string = get_class_string_from_dict('Info', info)
    class_string = """
    from typing import NamedTuple, List


class Employee(NamedTuple):
    id: int
    name: str


class Company(NamedTuple):
    id: int
    name: str
    employees: List[Employee]


class Info(NamedTuple):
    company: Company
    """.strip() + '\n'
    assert _class_string == class_string
