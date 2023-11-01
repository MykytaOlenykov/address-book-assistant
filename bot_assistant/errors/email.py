class InvalidEmail(Exception):
    def __init__(self, email, *args):
        super().__init__(*args)
        self.message = f"Email address {email} is invalid."


class EmailNotFound(Exception):
    def __init__(self, name, email, *args):
        super().__init__(*args)
        self.message = f"{name}`s record doesn`t contain {email} email address."


class EmailConflict(Exception):
    def __init__(self, name, email, *args):
        super().__init__(*args)
        self.message = f"{name}`s record contains {email} email address."
