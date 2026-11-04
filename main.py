
from checker import check_statement


source = """
Python was created by Guido van Rossum.
The Earth revolves around the Sun.
"""

statements = [
    "Python was created by Guido van Rossum.",
    "The Earth revolves around Mars.",
    "The Moon is made of cheese.",
]

for statement in statements:
    result = check_statement(statement, source)
    print(f"{statement} -> {result.value}")
