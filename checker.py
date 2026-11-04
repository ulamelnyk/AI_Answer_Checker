
from enum import Enum


class Status(Enum):
    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    UNSUPPORTED = "UNSUPPORTED"


def check_statement(statement, source):

    statement = statement.lower().strip()
    source = source.lower().strip()

    if statement in source:
        return Status.SUPPORTED

    return Status.UNSUPPORTED
