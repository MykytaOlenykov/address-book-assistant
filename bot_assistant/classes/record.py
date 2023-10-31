from bot_assistant.classes import Name
from bot_assistant.classes import Phone
from bot_assistant.errors import PhoneNotFound, PhoneConflict


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
