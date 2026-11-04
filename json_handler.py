
import json


def load_input(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_results(results, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
