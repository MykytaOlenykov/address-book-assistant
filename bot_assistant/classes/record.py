from bot_assistant.classes import Email, Name, Phone
from bot_assistant.errors import (
    PhoneNotFound,
    PhoneConflict,
    EmailNotFound,
    EmailConflict,
    InvalidEmail,
)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None
        self.note = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # phone
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

        raise PhoneNotFound(self.name, phone)

    def add_phone(self, new_phone):
        try:
            self.find_phone(new_phone)
        except PhoneNotFound:
            self.phones.append(Phone(new_phone))
        else:
            raise PhoneConflict(self.name, new_phone)

    def edit_phone(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        old_phone = self.find_phone(old_phone)

        try:
            self.find_phone(new_phone.value)
        except PhoneNotFound:
            old_phone.value = new_phone.value
        else:
            raise PhoneConflict(self.name.value, new_phone.value)

    def remove_phone(self, phone):
        filtered_phone = list(filter(lambda p: p.value != phone, self.phones))

        if len(filtered_phone) == len(self.phones):
            raise PhoneNotFound(self.name, phone)
        else:
            self.phones = filtered_phone

    # email
    def add_email(self, new_email):
        try:
            self.find_email(new_email)
        except EmailNotFound:
            self.emails.append(Email(new_email))
        else:
            raise EmailConflict(self.name, new_email)

    def del_email(self, email):
        filtered_email = list(filter(lambda p: p.value != email, self.emails))
        if len(filtered_email) == len(self.emails):
            raise EmailNotFound(self.name, email)
        else:
            self.emails = filtered_email

    def find_email(self, email):
        for email in self.emails:
            if email.value == email:
                return email

        raise EmailNotFound(self.name, email)

    def change_email(self, old_email, new_email):
        new_email = Email(new_email)
        old_email = self.find_email(old_email)
        try:
            self.find_email(new_email.value)
        except EmailNotFound:
            old_email.value = new_email.value
        else:
            raise EmailConflict(self.name.value, new_email.value)
