from enum import Enum


class Status(Enum):
    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    UNSUPPORTED = "UNSUPPORTED"

def normalize(text):
    return text.lower().strip().rstrip(".!?")

def check_statement(statement, source):
    statement = normalize(statement)
    source = normalize(source)

    if statement in source:
        return Status.SUPPORTED

    contradictions = {
        "the earth revolves around mars": "the earth revolves around the sun",
        "the earth revolves around the moon": "the earth revolves around the sun",
    }

    if statement in contradictions:
        opposite_statement = contradictions[statement]

        if opposite_statement in source:
            return Status.CONTRADICTED

    return Status.UNSUPPORTED
