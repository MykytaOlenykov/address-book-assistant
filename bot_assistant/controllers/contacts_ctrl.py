from bot_assistant.classes import Record
from bot_assistant.utils import input_error
from bot_assistant.errors import RecordNotFound


class ContactsCtrl:
    def show_all(book):
        if not book:
            return "Your phone book is empty."
        return book

    @input_error
    def add_contact(args, book):
        name, phone = args
        try:
            record = book.find_record(name)
        except RecordNotFound:
            new_record = Record(name)
            new_record.add_phone(phone)
            book.add_record(new_record)
        else:
            record.add_phone(phone)

        return "Contact added."
