from dataclasses import dataclass

from faker import Faker
from polyfactory.factories import DataclassFactory
from faker.providers.address.en_US import Provider

@dataclass
class UserDataClass:
    name: str
    surname: str
    email: str
    password: str
    gender: str
    date_of_birth: str
    address: str
    city: str
    state: str
    postal_code: str
    mobile_number: str


class UserFactory(DataclassFactory[UserDataClass]):
    __faker__ = Faker('en_US')
    __faker__.add_provider(Provider)

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

    @classmethod
    def address(cls):
        return cls.__faker__.street_address()

    @classmethod
    def city(cls):
        return cls.__faker__.city()

    @classmethod
    def state(cls):
        return cls.__faker__.administrative_unit()

    @classmethod
    def postal_code(cls):
        return cls.__faker__.postalcode()

    @classmethod
    def mobile_number(cls):
        return cls.__faker__.msisdn()
