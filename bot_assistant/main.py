from prompt_toolkit import prompt

from bot_assistant.classes import AddressBook
from bot_assistant.utils import parse_input, RainbowLexer, Completer
from bot_assistant.controllers import (
    AddressesCtrl,
    BirthdaysCtrl,
    ContactsCtrl,
    EmailsCtrl,
    NotesCtrl,
    PhonesCtrl,
)


def help():
    return (
        "----------------Main commands----------------------\n"
        "hello            |  greeting\n"
        "exit             |  exit the program\n"
        "close            |  exit the program\n"
        "help             |  show help information\n"
        "-----------------contacts --------------------------\n"
        "add-contact      |  add a contact and phone(s) number\n"
        "change-contact   |  change a contact\n"
        "show-contact     |  show a contact\n"
        "all              |  contacts with phones and birthdays\n"
        "delete-contact   |  delete contact/contact number\n"
        "-----------------phone number------------------------\n"
        "show-phone       |  show phone of a contact\n"
        "remove-phone     |  remove phone of a contact\n"
        "-----------------email address-----------------------\n"
        "add-email        |  add email to a contact\n"
        "show-email       |  show email of a contact\n"
        "change-email     |  change email in a contact\n"
        "remove-email     |  remove email of a contact\n"
        "-----------------address-----------------------------\n"
        "add-address      |  add address to a contact\n"
        "show-address     |  show address of a contact\n"
        "change-address   |  change address of a contact \n"
        "remove-address   |  remove address of a contact \n"
        "-----------------note--------------------------------\n"
        "add-note         |  add a note\n"
        "find-note        |  find a note\n"
        "show-note        |  show a note\n"
        "delete-note      |  delete a note\n"
        "add-tags         |  add tags to a note\n"
        "change-tag       |  change a tag of a note\n"
        "remove-tags      |  remove tags of a note\n"
        "-----------------birthday-----------------------------\n"
        "add-birthday     |  add birthday of a contact \n"
        "birthdays        |  show birthdays for next 7 days\n"
        "show-birthday    |  show birthday of a contact \n"
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
            user_input = prompt(
                ">>> Enter a command: ", completer=Completer, lexer=RainbowLexer()
            )
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                book.save_to_file(CONTACTS_FILENAME)
                print("Good bye!")
                break
            elif command == "help":
                print(help())
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
            elif command == "show-note":
                print(NotesCtrl.find_note_by_name(args, book))
            elif command == "find-notes":
                print(NotesCtrl.find_notes_by_tags(args, book))
            elif command == "add-note":
                print(NotesCtrl.add_note(args, book))
            elif command == "delete-note":
                print(NotesCtrl.delete_note(args, book))
            elif command == "add-tags":
                print(NotesCtrl.add_tags(args, book))
            elif command == "change-tag":
                print(NotesCtrl.change_tag(args, book))
            elif command == "remove-tags":
                print(NotesCtrl.remove_tags(args, book))

            # birthdays
            elif command == "birthdays":
                print(BirthdaysCtrl.birthdays(book))
            elif command == "add-birthday":
                print(BirthdaysCtrl.add_birthday(args, book))
            elif command == "show-birthday":
                print(BirthdaysCtrl.show_birthday(args, book))
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
