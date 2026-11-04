
import re
from enum import Enum


class Status(Enum):
    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    UNSUPPORTED = "UNSUPPORTED"


def normalize(text):
    return text.lower().strip().rstrip(".!?")


def extract_facts(text):
    facts = []

    sentences = re.split(r"[.!?]+", text.lower())

    for sentence in sentences:
        sentence = sentence.strip()

        # Pattern: "Python was created by Guido van Rossum"
        match = re.fullmatch(
            r"(.+?) was created by (.+)",
            sentence
        )

        if match:
            subject = match.group(1).strip()
            creator = match.group(2).strip()

            facts.append((subject, "created_by", creator))
            continue

        # Pattern: "Guido van Rossum created Python"
        match = re.fullmatch(
            r"(.+?) created (.+)",
            sentence
        )

        if match:
            creator = match.group(1).strip()
            subject = match.group(2).strip()

            facts.append((subject, "created_by", creator))
            continue

        # Pattern: "The Earth revolves around the Sun"
        match = re.fullmatch(
            r"(.+?) revolves around (.+)",
            sentence
        )

        if match:
            subject = match.group(1).strip()
            object_ = match.group(2).strip()

            facts.append((subject, "revolves_around", object_))

    return facts


def check_statement(statement, source):
    statement_normalized = normalize(statement)
    source_normalized = normalize(source)

    if statement_normalized in source_normalized:
        return Status.SUPPORTED

    source_facts = extract_facts(source)
    statement_facts = extract_facts(statement)

    for claim in statement_facts:
        for fact in source_facts:

            # Same subject and relation, same object
            if claim == fact:
                return Status.SUPPORTED

            # Same subject and relation, different object
            if claim[0] == fact[0] and claim[1] == fact[1]:
                return Status.CONTRADICTED

    return Status.UNSUPPORTED


def check_statements(statements, source):
    results = {}

    for statement in statements:
        results[statement] = check_statement(statement, source)

    return results


def get_confidence(status):
    confidence_scores = {
        Status.SUPPORTED: 1.0,
        Status.CONTRADICTED: 1.0,
        Status.UNSUPPORTED: 0.0,
    }

    return confidence_scores[status]
