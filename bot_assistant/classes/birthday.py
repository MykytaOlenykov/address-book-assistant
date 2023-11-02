from datetime import datetime, date

from bot_assistant.classes import Field
from bot_assistant.errors import InvalidBirthday, InvalidDate


class Birthday(Field):
    def __init__(self, value):
        self.birthday_validation(value)
        super().__init__(value)

    @Field.value.setter
    def value(self, value):
        self.birthday_validation(value)

        self._value = value

    def birthday_validation(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise InvalidDate
        else:
            if birthday_date > date.today():
                raise InvalidBirthday
