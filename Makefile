FLAKE8 ?= pipenv run flake8 --ignore=E501
MYPY ?= pipenv run mypy --pretty
PYTEST ?= pipenv run python -m pytest

all: flake8 mypy pytest

flake8:
	$(FLAKE8) classgen

mypy:
	$(MYPY) classgen

pytest:
	$(PYTEST)
