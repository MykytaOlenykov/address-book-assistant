class InvalidTag(Exception):
    def __init__(self, tag, *args):
        super().__init__(*args)
        self.message = f"Tag {tag} is invalid. The tag should be a length in the range of 1-30 and start with '#'."
