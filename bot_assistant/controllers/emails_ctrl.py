from bot_assistant.utils import input_error, create_table_header, create_table_row


class EmailsCtrl:
    @input_error
    def add_email_func(book):
        name = input("Please enter name: ")
        name = name.strip().title()
        if name not in book.data:
            return book, "\n<<< This user not in contact book.\n"
        contact = book[name]
        if contact.email:
            return book, "\n<<< Email for this contact already exist\n"
        email = input("Please enter email address: ")
        email = email.strip()
        contact.add_email(email)
        return book, f"\n<<< Email: [{email}] has been added to contact: [{name}]\n"

    def change_email_func(book):
        name = input("Please enter name: ")
        name = name.strip().title()
        if name not in book.data:
            return book, "\n<<< This user not in contact book.\n"
        contact = book[name]
        email = input("Please enter new email: ")
        email = email.strip()
        contact.add_email(email)
        return book, f"\n<<< Email: [{email}] has been changed to contact [{name}]\n"
