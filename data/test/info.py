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

