from checker import check_statements, get_confidence
from json_handler import load_input, save_results


def main():
    try:
        data = load_input("input.json")

        source = data["source"]
        statements = data["statements"]

        results = check_statements(statements, source)

        output = {
            "results": [
                {
                    "statement": statement,
                    "status": result.value,
                    "confidence": get_confidence(result)
                }
                for statement, result in results.items()
            ]
        }

        save_results(output, "output.json")

        print("Results saved to output.json")
        print("Results saved to results.json")

    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
