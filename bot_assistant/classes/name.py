from bot_assistant.classes import Field
from bot_assistant.errors import InvalidName


class Name(Field):
    def __init__(self, value):
        self.name_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self.name_validation(new_value)
        self._value = new_value

    def name_validation(self, name):
        if len(str(name)) < 2:
            raise InvalidName(name)
