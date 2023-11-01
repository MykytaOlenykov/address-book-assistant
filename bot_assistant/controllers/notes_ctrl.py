from bot_assistant.utils import input_error


class NotesCtrl:
    @input_error
    def find_note_by_name(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        note = record.note

        if not note:
            return f"{name}`s record doesn`t contain note."

        return note

    @input_error
    def add_note(args, book):
        if len(args) < 2:
            return "Give me name and note please."

        name = args[0]
        note = " ".join(args[1:])
        record = book.find_record(name)
        record.add_note(note)
        return "Note added."

    @input_error
    def delete_note(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        record = book.find_record(name)
        record.delete_note()
        return "Note deleted."
