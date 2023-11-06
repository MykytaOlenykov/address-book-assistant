from bot_assistant.utils import input_error
from bot_assistant.errors import InvalidTag, TagNotFound, TagConflict


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
    def find_notes_by_tags(args, book):
        if len(args) < 1:
            return "Give me tags please."

        found_notes = []

        for record_data in book.values():
            note = record_data.note

            if not note:
                continue

            for tag in args:
                try:
                    note.find_tag(tag)
                except TagNotFound:
                    continue
                else:
                    found_notes.append(str(note))
                    break

        return ("\n\n").join(found_notes)

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

    @input_error
    def add_tags(args, book):
        if len(args) < 2:
            return "Give me name and tags please."

        name = args[0]
        tags = args[1:]
        record = book.find_record(name)
        note = record.note

        if not note:
            return f"{name}`s record doesn`t contain note."

        invalid_tag_messages = ""
        tag_conflict_messages = ""
        count_of_error = 0

        for tag in tags:
            try:
                note.add_tag(tag)
            except InvalidTag as error:
                invalid_tag_messages += f"{error.message}\n"
                count_of_error += 1
            except TagConflict as error:
                tag_conflict_messages += f"{error.message}\n"
                count_of_error += 1

        info = ""

        if invalid_tag_messages:
            info += invalid_tag_messages
        if tag_conflict_messages:
            info += tag_conflict_messages

        info = info.removesuffix("\n")

        if len(tags) == count_of_error:
            return info
        elif info:
            return f"Some tags added, but:\n{info}"
        else:
            return "Tags added."

    @input_error
    def change_tag(args, book):
        if len(args) != 3:
            return "Give me name, old tag and new tag please."

        name, old_tag, new_tag = args
        record = book.find_record(name)
        note = record.note
        note.edit_tag(old_tag, new_tag)
        return "Tag updated."

    @input_error
    def remove_tags(args, book):
        if len(args) < 2:
            return "Give me name and tags please."

        name = args[0]
        tags = args[1:]
        record = book.find_record(name)
        note = record.note

        if not note:
            return f"{name}`s record doesn`t contain note."

        tag_conflict_messages = ""
        count_of_error = 0

        for tag in tags:
            try:
                note.remove_tag(tag)
            except TagNotFound as error:
                tag_conflict_messages += f"{error.message}\n"
                count_of_error += 1

        info = ""

        if tag_conflict_messages:
            info += tag_conflict_messages

        info = info.removesuffix("\n")

        if len(tags) == count_of_error:
            return info
        elif info:
            return f"Some tags removed, but:\n{info}"
        else:
            return "Tags removed."
