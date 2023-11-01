from bot_assistant.utils import input_error


class AddressesCtrl:
    @input_error
    def find_address(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        address = record.address

        if address:
            return f"{name} has address: {address}"
        else:
            return "Address not found."

    @input_error
    def add_address(args, book):
        if len(args) < 2:
            return "Give me name and address please."

        name = args[0]
        address = " ".join(args[1:])
        record = book.find_record(name)
        record.add_address(address)
        return f"Address created."

    @input_error
    def change_address(args, book):
        if len(args) < 2:
            return "Give me name and new address please."

        name = args[0]
        address = " ".join(args[1:])
        record = book.find_record(name)
        record.change_address(address)
        return f"Address changed."

    @input_error
    def remove_address(args, book):
        if len(args) != 1:
            return "Gime me name please."

        name = args[0]
        record = book.find_record(name)
        record.remove_address()
        return "Address removed."
