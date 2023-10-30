class InvalidName(Exception):
    def __init__(self, name, *args):
        super().__init__(*args)
        self.message = f"Name {name} is invalid. The minimum length of the name must be 2 characters."
