
from checker import check_statements


print("=== AI Answer Checker ===")

source = input("\nEnter source text:\n")

print("\nEnter statements to check.")
print("Type 'done' when finished.\n")

statements = []

while True:
    statement = input("Statement: ")

    if statement.lower() == "done":
        break

    statements.append(statement)

results = check_statements(statements, source)

print("\n=== Results ===")

for statement, result in results.items():
    print(f"{statement} -> {result.value}")
