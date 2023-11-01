from bot_assistant.utils import input_error, create_table_header, create_table_row


class EmailsCtrl:
    @input_error
    def find_email(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        emails = record.emails

        table = create_table_header(name)

        if not emails:
            return table + create_table_row("Empty")

        for email in emails:
            table += create_table_row(email.value) + "\n"

        return table.removesuffix("\n")

    @input_error
    def add_email(args, book):
        if len(args) != 2:
            return "Give me name and email please."

        name, email = args
        record = book.find_record(name)
        record.add_email(email)

        return "Email added."

    @input_error
    def change_email(args, book):
        if len(args) != 3:
            return "Give me name, old email and new email please."

        name, old_email, new_email = args
        record = book.find_record(name)
        record.edit_email(old_email, new_email)
        return "Email updated."

    @input_error
    def remove_email(args, book):
        if len(args) != 2:
            return "Give me name and email please."

        name, email = args
        record = book.find_record(name)
        record.remove_email(email)
        return "Email removed."
