from classgen.parsers import get_object_from_dict


def test_get_object_from_dict():
    _company = {
        'id': 1,
        'name': 'example corporation'
    }
    company = get_object_from_dict('company', **_company)

    assert company.__class__.__name__ == 'Company'
    assert company.id == _company['id']
    assert company.name == _company['name']

    _info = {
        'company': {
            'id': 1,
            'name': 'example corporation'
        }
    }
    info = get_object_from_dict('info', **_info)

    assert info.__class__.__name__ == 'Info'
    assert hasattr(info, 'company')
    assert info.company.__class__.__name__ == 'Company'
    assert info.company.id == _info['company']['id']
    assert info.company.name == _info['company']['name']

    _info = {
        'company': {
            'id': 1,
            'name': 'example corporation',
            'employees': [
                'tanaka',
                'yamada'
            ]
        }
    }
    info = get_object_from_dict('info', **_info)

    assert info.__class__.__name__ == 'Info'
    assert hasattr(info, 'company')
    assert info.company.__class__.__name__ == 'Company'
    assert info.company.id == _info['company']['id']
    assert info.company.name == _info['company']['name']
    assert info.company.employees == _info['company']['employees']

    _info = {
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
    info = get_object_from_dict('info', **_info)

    assert info.__class__.__name__ == 'Info'
    assert hasattr(info, 'company')
    assert info.company.__class__.__name__ == 'Company'
    assert info.company.id == _info['company']['id']
    assert info.company.name == _info['company']['name']
    for i, employee in enumerate(info.company.employees):
        assert employee.__class__.__name__ == 'Employee'
        assert employee.id == _info['company']['employees'][i]['id']
        assert employee.name == _info['company']['employees'][i]['name']
