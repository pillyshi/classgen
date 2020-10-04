import yaml

from data.test.info import Employee, Company, Info
from classgen.loaders import load_yaml


def test_load_yaml():
    classes = [Employee, Company, Info]
    with open('data/test/info.yml') as f:
        _info = yaml.safe_load(f)
    with open('data/test/info.yml') as f:
        info = load_yaml(f, Info, classes)
    assert info.__class__ == Info
    assert hasattr(info, 'company')
    assert info.company.__class__.__name__ == 'Company'
    assert info.company.id == _info['company']['id']
    assert info.company.name == _info['company']['name']
    for i, employee in enumerate(info.company.employees):
        assert employee.__class__.__name__ == 'Employee'
        assert employee.id == _info['company']['employees'][i]['id']
        assert employee.name == _info['company']['employees'][i]['name']


def test_load_json():
    classes = [Employee, Company, Info]
    with open('data/test/info.json') as f:
        _info = yaml.safe_load(f)
    with open('data/test/info.json') as f:
        info = load_yaml(f, Info, classes)
    assert info.__class__ == Info
    assert hasattr(info, 'company')
    assert info.company.__class__.__name__ == 'Company'
    assert info.company.id == _info['company']['id']
    assert info.company.name == _info['company']['name']
    for i, employee in enumerate(info.company.employees):
        assert employee.__class__.__name__ == 'Employee'
        assert employee.id == _info['company']['employees'][i]['id']
        assert employee.name == _info['company']['employees'][i]['name']
