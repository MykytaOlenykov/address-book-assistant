class InvalidAddress(Exception):
    def __init__(self, address, *args):
        super().__init__(*args)
        self.message = f"Address {address} is invalid. You can't use special\
              symbols."
