import re

from bot_assistant.classes import Field


class Address(Field):
    ADDRESS_FORMAT = r"[A-Za-z0-9'\.\-\s\,]"

    def __init__(self, value):
        self.address_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self.address_validation(new_value)
        self.value = new_value

    def address_validation(self, address):
        if not re.fullmatch(self.ADDRESS_FORMAT, address):
            raise InvalidAddress(address)
