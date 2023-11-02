from bot_assistant.utils import input_error, create_table_header, create_table_row


class PhonesCtrl:
    @input_error
    def find_phone(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        phones = record.phones

        table = create_table_header("Phones")

        if not phones:
            return table + create_table_row("Empty")

        for phone in phones:
            table += create_table_row(phone.value) + "\n"

        return table.removesuffix("\n")

    @input_error
    def remove_phone(args, book):
        if len(args) != 2:
            return "Give me name and phone please."

        name, phone = args
        record = book.find_record(name)
        record.remove_phone(phone)
        return "Phone removed."
