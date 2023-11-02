import pickle
from datetime import datetime
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

    def delete_record(self, name):
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

    def get_birthdays_per_week(self):
        week_days = {
            "Monday": [],
            "Tuersday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
        }
        today = datetime.today().date()
        birthday_info = []
        for name, record in self.data.items():
            if not record.birthday:
                continue
            birthday_obj = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday_obj.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_obj.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                weekday = birthday_this_year.weekday()
                if weekday in [0, 5, 6]:
                    week_days["Monday"].append(name)
                elif weekday == 1:
                    week_days["Tuersday"].append(name)
                elif weekday == 2:
                    week_days["Wednesday"].append(name)
                elif weekday == 3:
                    week_days["Thursday"].append(name)
                elif weekday == 4:
                    week_days["Friday"].append(name)

        for key, value in week_days.items():
            if value != []:
                birthday_info.append(f"{key}: {', '.join(value)}\n")
        if birthday_info:
            return "".join(birthday_info).removesuffix("\n")
        else:
            return "Next week birthays not found"
