from bot_assistant.errors.name import InvalidName
from bot_assistant.errors.phone import InvalidPhone, PhoneNotFound, PhoneConflict
from bot_assistant.errors.record import RecordNotFound, RecordConflict
from bot_assistant.errors.email import InvalidEmail, EmailNotFound, EmailConflict

__all__ = [
    "InvalidName",
    "InvalidPhone",
    "PhoneNotFound",
    "PhoneConflict",
    "RecordNotFound",
    "RecordConflict",
    "InvalidEmail",
    "EmailNotFound",
    "EmailConflict",
]
