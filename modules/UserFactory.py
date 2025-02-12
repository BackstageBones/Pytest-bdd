
from dataclasses import dataclass
from faker import Faker
from polyfactory.factories import DataclassFactory


@dataclass
class UserDataClass:
    name: str
    surname: str
    email: str
    password: str
    gender: str
    date_of_birth: str


class UserFactory(DataclassFactory[UserDataClass]):
    __faker__ = Faker('en_US')

    @classmethod
    def name(cls):
        return cls.__faker__.first_name()

    @classmethod
    def surname(cls):
        return cls.__faker__.last_name()

    @classmethod
    def email(cls):
        return cls.__faker__.email()

    @classmethod
    def password(cls):
        return cls.__faker__.password(length=6)

    @classmethod
    def gender(cls):
        return cls.__faker__.passport_gender(seed=2)

    @classmethod
    def date_of_birth(cls):
        return cls.__faker__.date_of_birth()
