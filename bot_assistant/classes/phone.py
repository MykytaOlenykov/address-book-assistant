from bot_assistant.classes import Field
from bot_assistant.errors import InvalidPhone


class Phone(Field):
    def __init__(self, value):
        self.phone_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self.phone_validation(new_value)
        self._value = new_value

    def phone_validation(self, phone):
        if len(str(phone)) != 10:
            raise InvalidPhone(phone)
