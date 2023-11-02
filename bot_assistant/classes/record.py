from bot_assistant.utils import create_table_header, create_table_row
from bot_assistant.classes import (
    Email,
    Name,
    Phone,
    Address,
    Note,
    Birthday,
)
from bot_assistant.errors import (
    PhoneNotFound,
    PhoneConflict,
    EmailNotFound,
    EmailConflict,
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
        empty_field = "-\n\n"
        empty_row = create_table_row("Empty")
        info = f"Name: {self.name.value}\n\n"

        info += f"Address: "
        if self.address:
            info += f"{self.address.value}\n\n"
        else:
            info += empty_field

        info += f"Birthday: "
        if self.birthday:
            info += f"{self.birthday.value}\n\n"
        else:
            info += empty_field

        if self.note:
            info += f"{self.note}\n\n"
        else:
            info += f"Note: {empty_field}"

        info += create_table_header("Phones")
        if not self.phones:
            info += empty_row + "\n"
        else:
            for phone in self.phones:
                info += create_table_row(phone.value) + "\n"

        info += "\n" + create_table_header("Emails")
        if not self.emails:
            info += empty_row + "\n"
        else:
            for email in self.emails:
                info += create_table_row(email.value) + "\n"

        return info.removesuffix("\n")

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
        filtered_phones = list(filter(lambda p: p.value != phone, self.phones))

        if len(filtered_phones) == len(self.phones):
            raise PhoneNotFound(self.name, phone)
        else:
            self.phones = filtered_phones

    # email
    def add_email(self, new_email):
        try:
            self.find_email(new_email)
        except EmailNotFound:
            self.emails.append(Email(new_email))
        else:
            raise EmailConflict(self.name, new_email)

    def remove_email(self, email):
        filtered_emails = list(filter(lambda e: e.value != email, self.emails))
        if len(filtered_emails) == len(self.emails):
            raise EmailNotFound(self.name, email)
        else:
            self.emails = filtered_emails

    def find_email(self, email):
        for e in self.emails:
            if e.value == email:
                return e

        raise EmailNotFound(self.name, email)

    def edit_email(self, old_email, new_email):
        new_email = Email(new_email)
        old_email = self.find_email(old_email)
        try:
            self.find_email(new_email.value)
        except EmailNotFound:
            old_email.value = new_email.value
        else:
            raise EmailConflict(self.name.value, new_email.value)

    # address
    def add_address(self, address):
        self.address = Address(address)

    def change_address(self, address):
        self.address = Address(address)

    def remove_address(self):
        self.address = None

    # note
    def add_note(self, note):
        self.note = Note(note)

    def delete_note(self):
        self.note = None

    # birthday
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return "Birthday added"
