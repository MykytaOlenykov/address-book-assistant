class InvalidBirthday(Exception):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.message = f"Birthday:{value} must be less than current year and date"


class InvalidDate(Exception):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.message = f"Wrong birthday date:{value} Please, input DD.MM.YYYY"
