from bot_assistant.utils import input_error
from bot_assistant.classes import Record


class AddressesCtrl:
    @input_error
    def find_address(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        if not record:
            return f"{name} not found"
        address = record.address

        if address:
            return f"{name} has address: {address}"
        else:
            return "Address not found"

    def add_address(args, book):
        if len(args) < 2:
            return "Give me name and address please."

        name = args[0]
        address = " ".join(args[1:])
        record: Record = book.find_record(name)
        if not record:
            return f"{name} not found."
        record.add_address(address)
        return f"Address created."

    def change_address(args, book):
        if len(args) < 2:
            return "Give me name and new address please."
        name = args[0]
        address = " ".join(args[1:])
        record: Record = book.find_record(name)
        if not record:
            return f"{name} not found."
        record.change_address(address)
        return f"Address changed."

    def remove_address(args, book):
        if len(args) != 1:
            return "Gime me valid name please."
        name = args[0]
        record: Record = book.find_record(name)
        if not record:
            return f"{name} not found."
        record.remove_address()
        return "Address removed."
