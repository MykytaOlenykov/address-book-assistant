from bot_assistant.classes import Record
from bot_assistant.utils import input_error
from bot_assistant.errors import RecordNotFound


class ContactsCtrl:
    def show_all(book):
        if not book:
            return "Your phone book is empty."
        return book

    @input_error
    def find_contact(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        return book.find_record(name)

    @input_error
    def add_contact(args, book):
        if len(args) != 2:
            return "Give me name and phone please."

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

    @input_error
    def change_contact(args, book):
        if len(args) != 3:
            return "Give me name, old phone and new phone please."

        name, old_phone, new_phone = args
        record = book.find_record(name)
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."

    @input_error
    def delete_contact(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        book.delete(name)
        return "Contact deleted."
