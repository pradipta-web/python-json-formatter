```markdown
# Python JSON Formatter & Validator

A simple Python tool to validate, format, and export JSON files.

## Features

- Validate JSON file syntax.
- Detect invalid JSON formats.
- Format JSON with proper indentation.
- Display formatted JSON in the terminal.
- Export formatted JSON to a new file.

## Technologies

- Python 3
- JSON Module
- OS Module

## Project Structure

```text
python-json-formatter/
├── app.py
├── sample.json
├── requirements.txt
├── README.md
├── .gitignore
└── formatted_output.json
```

## Installation

Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-json-formatter.git
```

Navigate to the project directory:

```bash
cd python-json-formatter
```

## Usage

Run the application:

```bash
py app.py
```

Enter your JSON file path when prompted:

```text
sample.json
```

The application will validate and format the JSON file, then save the result as:

```text
formatted_output.json
```

## Example Output

```text
=============================================
       PYTHON JSON FORMATTER
=============================================

Enter JSON file path: sample.json

[ SUCCESS ] JSON file is valid!

[ SUCCESS ] Formatted JSON saved to formatted_output.json
```

## Author

**Kinervaaa**

GitHub: https://github.com/pradipta-web
```