from bot_assistant.classes import Field, Tag
from bot_assistant.utils import create_table_header, create_table_row
from bot_assistant.errors import TagNotFound, TagConflict


class Note(Field):
    def __init__(self, value):
        super().__init__(value)
        self.tags = []

    def __str__(self):
        tags = f"Tags: {', '.join(t.value for t in self.tags)}"
        return f"{tags}\nNote: {self.value}"

    def find_tag(self, tag):
        for t in self.tags:
            if t.value == tag:
                return t

        raise TagNotFound(tag)

    def add_tag(self, new_tag):
        try:
            self.find_tag(new_tag)
        except TagNotFound:
            self.tags.append(Tag(new_tag))
        else:
            raise TagConflict(new_tag)

    def edit_tag(self, old_tag, new_tag):
        new_tag = Tag(new_tag)
        old_tag = self.find_tag(old_tag)

        try:
            self.find_tag(new_tag.value)
        except TagNotFound:
            old_tag.value = new_tag.value
        else:
            raise TagConflict(new_tag.value)

    def remove_tag(self, tag):
        filtered_tags = list(filter(lambda t: t.value != tag, self.tags))

        if len(filtered_tags) == len(self.tags):
            raise TagNotFound(tag)
        else:
            self.tags = filtered_tags
