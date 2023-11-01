import re
from bot_assistant.classes import Field
from bot_assistant.errors import InvalidEmail


class Email(Field):
    PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    def __init__(self, value):
        self.email_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self.email_validation(new_value)
        self._value = new_value

    def email_validation(self, email):
        if not re.fullmatch(self.PATTERN, str(email)):
            raise InvalidEmail(email)
