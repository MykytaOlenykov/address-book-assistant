from bot_assistant.classes import Field
import re


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    @Field.value.setter
    def value(self, value):
        if value == "There are no phone numbers.":
            self._value = value
        else:
            pattern = r"\+\d{12}"
            phone = re.findall(pattern, value)
            if phone:
                self._value = phone[0]
