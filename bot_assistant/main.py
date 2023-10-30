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
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input(">>> Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(placeholder())
                break
            elif command == "help":
                print(placeholder())
            elif command == "hello":
                print("How can I help you?")

            # contacts
            elif command == "all":
                # print(AddressesCtrl.show_all())
                print(placeholder())
            elif command == "add-contact":
                print(placeholder())
            elif command == "change-contact":
                print(placeholder())
            elif command == "delete-contact":
                print(placeholder())

            # phone
            elif command == "find-phone":
                print(placeholder())
            elif command == "remove-phone":
                print(placeholder())

            # email
            elif command == "find-email":
                print(placeholder())
            elif command == "add-email":
                print(placeholder())
            elif command == "change-email":
                print(placeholder())
            elif command == "remove-email":
                print(placeholder())

            # address
            elif command == "find-address":
                print(placeholder())
            elif command == "add-address":
                print(placeholder())
            elif command == "change-address":
                print(placeholder())
            elif command == "remove-address":
                print(placeholder())

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
        except:
            print("Something went wrong.")
            break


if __name__ == "__main__":
    main()
