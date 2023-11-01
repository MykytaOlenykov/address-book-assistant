from bot_assistant.classes import AddressBook
from bot_assistant.utils import parse_input
from bot_assistant.controllers import (
    AddressesCtrl,
    BirthdaysCtrl,
    ContactsCtrl,
    EmailsCtrl,
    NotesCtrl,
    PhonesCtrl,
)

CONTACTS_FILENAME = "contacts.bin"


def placeholder():
    return "This command is under development"


def main():
    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input(">>> Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                book.save_to_file(CONTACTS_FILENAME)
                print("Good bye!")
                break
            elif command == "help":
                print(placeholder())
            elif command == "hello":
                print("How can I help you?")

            # contacts
            elif command == "all":
                print(ContactsCtrl.show_all(book))
            elif command == "show-contact":
                print(ContactsCtrl.find_contact(args, book))
            elif command == "add-contact":
                print(ContactsCtrl.add_contact(args, book))
            elif command == "change-contact":
                print(ContactsCtrl.change_contact(args, book))
            elif command == "delete-contact":
                print(ContactsCtrl.delete_contact(args, book))

            # phone
            elif command == "show-phone":
                print(PhonesCtrl.find_phone(args, book))
            elif command == "remove-phone":
                print(PhonesCtrl.remove_phone(args, book))

            # email
            elif command == "show-email":
                print(EmailsCtrl.find_email(args, book))
            elif command == "add-email":
                print(EmailsCtrl.add_email(args, book))
            elif command == "change-email":
                print(EmailsCtrl.change_email(args, book))
            elif command == "remove-email":
                print(EmailsCtrl.remove_email(args, book))

            # address
            elif command == "show-address":
                print(AddressesCtrl.find_address(args, book))
            elif command == "add-address":
                print(AddressesCtrl.add_address(args, book))
            elif command == "change-address":
                print(AddressesCtrl.change_address(args, book))
            elif command == "remove-address":
                print(AddressesCtrl.remove_address(args, book))

            # note
            elif command == "add-note":
                print(placeholder())
            elif command == "find-note":
                print(placeholder())
            elif command == "clear-note":
                print(placeholder())
            elif command == "add-tags":
                print(placeholder())
            elif command == "change-tag":
                print(placeholder())
            elif command == "remove-tags":
                print(placeholder())

            # birthdays
            elif command == "birthdays":
                print(placeholder())
            elif command == "add-birthday":
                print(placeholder())
            elif command == "show-birthday":
                print(placeholder())
            else:
                print("Invalid command.")
        except KeyboardInterrupt:
            print("\nInvalid command.")
        # except:
        #     book.save_to_file(CONTACTS_FILENAME)
        #     print("Something went wrong.")
        #     break


if __name__ == "__main__":
    main()
