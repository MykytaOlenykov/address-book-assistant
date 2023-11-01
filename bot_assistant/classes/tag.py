from bot_assistant.classes import Field
from bot_assistant.errors import InvalidTag


class Tag(Field):
    def __init__(self, value):
        self.tag_validation(value)
        super().__init__(value)

    def value(self, new_value):
        self.tag_validation(new_value)
        self._value = new_value

    def tag_validation(self, tag: str):
        if not tag.startswith("#") or len(tag) > 30:
            raise InvalidTag(tag)
