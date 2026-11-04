# AI Answer Checker

A Python-based tool for evaluating AI-generated statements against a source text. The project explores AI reliability, factual verification, and software testing through a simple rule-based approach.

## Overview

AI systems can generate statements that sound convincing but are incorrect or unsupported by available information. This project explores a basic approach to checking AI-generated claims against a provided source.

The checker classifies statements into three categories:

- **SUPPORTED** – the statement is supported by the provided source text or recognized fact patterns.
- **CONTRADICTED** – the statement conflicts with information found in the source through predefined rules.
- **UNSUPPORTED** – the statement cannot be verified or contradicted using the current implementation.

## Features

- Check multiple statements against one source.
- Basic fact extraction using predefined patterns.
- Rule-based contradiction detection.
- Basic paraphrase recognition.
- Case-insensitive text matching.
- Text normalization for punctuation and whitespace.
- JSON input and output support.
- Rule-based confidence scores.
- Error handling for invalid or missing JSON files.
- Automated unit tests using pytest.

## Technologies

- Python 3
- pytest
- JSON
- Git & GitHub

## Project Structure

```text
AI_Answer_Checker/
│
├── main.py           # Main application
├── checker.py        # Statement checking logic
├── json_handler.py   # JSON input and output handling
├── test_checker.py   # Automated tests
├── input.json        # Input source and statements
├── results.json      # Generated verification results
├── requirements.txt  # Project dependencies
├── .gitignore       # Git ignored files
└── README.md         # Project documentation
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ulamelnyk/AI_Answer_Checker.git
cd AI_Answer_Checker
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

### 1. Prepare the input

Open `input.json` and provide a source text and statements to verify.

Example:

```json
{
  "source": "Python was created by Guido van Rossum.",
  "statements": [
    "Guido van Rossum created Python.",
    "Python was created by Elon Musk.",
    "Python is popular in data science."
  ]
}
```

### 2. Run the application

```bash
python3 main.py
```

### 3. View the results

The application generates a `results.json` file containing the verification results.

Example:

```json
[
    {
        "statement": "Guido van Rossum created Python.",
        "status": "SUPPORTED",
        "confidence": 1.0
    },
    {
        "statement": "Python was created by Elon Musk.",
        "status": "CONTRADICTED",
        "confidence": 1.0
    },
    {
        "statement": "Python is popular in data science.",
        "status": "UNSUPPORTED",
        "confidence": 0.0
    }
]
```

## Running Tests

The project includes automated tests for checking statements, contradiction detection, fact extraction, and basic edge cases.

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

## Current Limitations

This project currently uses a rule-based approach rather than a language model or advanced semantic reasoning system.

- Supported statements are detected through text matching and predefined fact extraction patterns.
- Contradictions are recognized only through explicitly defined rules.
- Paraphrase recognition is limited to predefined patterns and may not cover more complex rewordings.
- The checker cannot independently verify facts against external sources.
- Confidence scores reflect rule matching rather than actual factual certainty.
- Results depend on the provided source text and implemented rules.

A statement classified as **UNSUPPORTED** is not necessarily false. It simply cannot be verified using the current implementation.

## Future Improvements

Planned development:

- Expand fact extraction patterns.
- Improve paraphrase recognition.
- Add more comprehensive contradiction rules.
- Develop an evaluation dataset.
- Calculate accuracy, precision, and recall.
- Explore semantic similarity and NLP-based verification.
- Compare rule-based verification with semantic approaches.
