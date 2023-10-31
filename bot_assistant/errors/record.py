class RecordNotFound(Exception):
    def __init__(self, name, *args):
        super().__init__(*args)
        self.message = f"A person with name {name} is not in your phone book."


class RecordConflict(Exception):
    def __init__(self, name, *args):
        super().__init__(*args)
        self.message = f"A person with name {name} already exists."
