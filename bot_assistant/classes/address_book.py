import pickle

from pathlib import Path
from collections import UserDict

from bot_assistant.errors import RecordNotFound, RecordConflict


class AddressBook(UserDict):
    __PATH_CONTACTS_DB = Path(__file__).parent / ".." / "db"

    def __str__(self):
        return "".join([f"{record}\n" for record in self.data.values()]).rstrip("\n")

    def find_record(self, name):
        if not name in self.data:
            raise RecordNotFound(name)
        else:
            return self.data[name]

    def add_record(self, record):
        name = record.name.value

        if name in self.data:
            raise RecordConflict(name)
        else:
            self.data[name] = record

    def delete(self, name):
        if not name in self.data:
            raise RecordNotFound(name)
        else:
            self.data.pop(name)

    def save_to_file(self, filename):
        with open(self.__PATH_CONTACTS_DB / filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filename):
        path = self.__PATH_CONTACTS_DB / filename

        if not path.exists():
            return

        with open(path, "rb") as fh:
            self.data = pickle.load(fh)
