from bot_assistant.errors import (
    InvalidName,
    InvalidPhone,
    PhoneNotFound,
    PhoneConflict,
    RecordNotFound,
    RecordConflict,
    InvalidEmail,
    EmailNotFound,
    EmailConflict,
    InvalidAddress,
    InvalidTag,
    TagNotFound,
    TagConflict,
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidName as error:
            return error.message
        except InvalidPhone as error:
            return error.message
        except PhoneNotFound as error:
            return error.message
        except PhoneConflict as error:
            return error.message
        except InvalidEmail as error:
            return error.message
        except EmailNotFound as error:
            return error.message
        except EmailConflict as error:
            return error.message
        except InvalidAddress as error:
            return error.message
        except InvalidTag as error:
            return error.message
        except TagNotFound as error:
            return error.message
        except TagConflict as error:
            return error.message
        except RecordNotFound as error:
            return error.message
        except RecordConflict as error:
            return error.message

    return inner
