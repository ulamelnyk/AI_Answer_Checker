
from checker import check_statement, Status


def test_supported_statement():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "The Earth revolves around the Sun.",
        source
    )

    assert result == Status.SUPPORTED


def test_contradicted_statement():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "The Earth revolves around Mars.",
        source
    )

    assert result == Status.CONTRADICTED


def test_unsupported_statement():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "The Moon is made of cheese.",
        source
    )

    assert result == Status.UNSUPPORTED


def test_case_insensitive_matching():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "THE EARTH REVOLVES AROUND THE SUN.",
        source
    )

    assert result == Status.SUPPORTED


def test_statement_without_punctuation():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "The Earth revolves around the Sun",
        source
    )

    assert result == Status.SUPPORTED


def test_extra_spaces():
    source = "The Earth revolves around the Sun."

    result = check_statement(
        "  The Earth revolves around the Sun.  ",
        source
    )

    assert result == Status.SUPPORTED
