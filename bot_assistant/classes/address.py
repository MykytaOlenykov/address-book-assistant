from bot_assistant.classes import Field
from bot_assistant.errors import InvalidAddress


class Address(Field):
    def __init__(self, value):
        self.address_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self.address_validation(new_value)
        self.value = new_value

    def address_validation(self, address):
        if len(address) <= 5 or len(address) >= 100:
            raise InvalidAddress(address)
