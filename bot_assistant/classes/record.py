from bot_assistant.classes import Email


class Record:
    def __init__(self, name):
        self.email = None

    def add_email(self, email_data: str):
        """Adds an email address"""
        self.email = Email(email_data)

    def del_email(self):
        """Deletes an email address"""
        self.email = None
