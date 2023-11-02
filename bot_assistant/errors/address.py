class InvalidAddress(Exception):
    def __init__(self, address, *args):
        super().__init__(*args)
        self.message = f"Address {address} is invalid. The address should be a length in the range of 5-100."
