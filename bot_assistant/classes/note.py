from bot_assistant.classes import Field
from bot_assistant.utils import create_table_header, create_table_row


class Note(Field):
    def __init__(self, value):
        super().__init__(value)
        self.tags = []

    def __str__(self):
        table = create_table_header("Tags")

        if not self.tags:
            table_body = create_table_row("Empty")
            return f"{table}{table_body}\n\nNote: {self.value}"

        for tag in self.tags:
            table += create_table_row(tag) + "\n"

        return f"{table}\nNote: {self.value}"

    def find_tag():
        pass

    def add_tag():
        pass

    def edit_tag():
        pass

    def remove_tag():
        pass
