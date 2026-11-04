# AI Answer Checker

A Python-based tool for evaluating AI-generated statements against a source text. The project is designed to explore AI reliability, factual verification, and software testing through a simple rule-based approach.

## Overview

AI systems can generate statements that sound convincing but are incorrect or unsupported by available information. This project explores a basic approach to checking AI-generated claims against a provided source.

The checker classifies statements into three categories:

- **SUPPORTED** - the statement is found in the source text.
- **CONTRADICTED** - the statement matches a predefined contradiction rule against information in the source.
- **UNSUPPORTED** - the statement is neither supported nor recognized as contradicted.

## Features

- Check multiple statements against one source.
- Interactive command-line interface.
- Basic contradiction detection using predefined rules.
- Case-insensitive text matching.
- Text normalization for punctuation differences.
- Automated unit tests using pytest.

## Technologies

- Python 3
- pytest
- Git & GitHub

## Project Structure

```text
AI_Answer_Checker/
│
├── main.py           # Interactive command-line application
├── checker.py        # Statement checking logic
├── test_checker.py   # Automated tests
├── requirements.txt  # Project dependencies
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
pip3 install pytest
```

## Usage

Run the application:

```bash
python3 main.py
```

### Example

```text
=== AI Answer Checker ===

Enter source text:
Python was created by Guido van Rossum.
Python is a programming language.

Enter statements to check.
Type 'done' when finished.

Statement: Python was created by Guido van Rossum.
Statement: Python was created by Elon Musk.
Statement: The Moon is made of cheese.
Statement: done

=== Results ===

Python was created by Guido van Rossum. -> SUPPORTED
Python was created by Elon Musk. -> UNSUPPORTED
The Moon is made of cheese. -> UNSUPPORTED
```

## Running Tests

The project includes automated tests for checking statements and handling basic edge cases.

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

## Current Limitations

This project currently uses a simple rule-based approach rather than a language model or semantic reasoning system.

- Supported statements are detected through text matching.
- Contradictions are recognized only through explicitly defined rules.
- Paraphrases may not be recognized as supported.
- The checker cannot independently verify facts against external sources.
- Results depend on the provided source text and implemented rules.

A statement classified as unsupported is not necessarily false. It simply cannot be verified using the current implementation.

## Future Improvements

Planned development:

- Improve text matching and normalization.
- Expand contradiction detection.
- Add confidence scores.
- Support structured input and output.
- Introduce semantic similarity.
- Explore NLP-based claim verification.
- Evaluate performance on a collection of test examples.
