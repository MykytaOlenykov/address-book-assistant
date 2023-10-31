from bot_assistant.classes import Field
import re
from bot_assistant.errors import RecordNotFound


class Email(Field):
    """Make a regular expression for validating an Email"""

    @Field.value.setter
    def find_email(self, value):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        email = re.findall(pattern, value)
        if not email:
            raise ValueError("Invalid Email")
        self._value = email

    def find_record(self, name):
        if not name in self.data:
            raise RecordNotFound(name)
        else:
            return self.data[name]
