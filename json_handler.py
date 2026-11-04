
import json


def load_input(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{filename}' was not found.")

    except json.JSONDecodeError:
        raise ValueError(f"Input file '{filename}' contains invalid JSON.")


def save_results(results, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
