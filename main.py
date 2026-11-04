
from checker import check_statements
from json_handler import load_input, save_results


data = load_input("input.json")

source = data["source"]
statements = data["statements"]

results = check_statements(statements, source)

output = {
    "results": [
        {
            "statement": statement,
            "status": result.value
        }
        for statement, result in results.items()
    ]
}

save_results(output, "results.json")

print("Checking completed!")
print("Results saved to results.json")
