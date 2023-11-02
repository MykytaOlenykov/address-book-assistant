class InvalidTag(Exception):
    def __init__(self, tag, *args):
        super().__init__(*args)
        self.message = f"Tag {tag} is invalid. The tag should be a length in the range of 2-30 and start with '#'."


class TagNotFound(Exception):
    def __init__(self, tag, *args):
        super().__init__(*args)
        self.message = f"This note doesn`t contain {tag} tag."


class TagConflict(Exception):
    def __init__(self, tag, *args):
        super().__init__(*args)
        self.message = f"This note contains {tag} tag."
