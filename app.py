import json
import os


def validate_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n[ SUCCESS ] JSON file is valid!")
        return data

    except FileNotFoundError:
        print("\n[ ERROR ] File not found!")

    except json.JSONDecodeError as error:
        print("\n[ ERROR ] Invalid JSON format!")
        print(f"Details: {error}")

    return None


def format_json(data):
    formatted_data = json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )

    return formatted_data


def save_json(formatted_data):
    output_file = "formatted_output.json"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(formatted_data)

    print(f"\n[ SUCCESS ] Formatted JSON saved to {output_file}")


def main():
    print("=" * 45)
    print("       PYTHON JSON FORMATTER")
    print("=" * 45)

    file_path = input("\nEnter JSON file path: ")

    data = validate_json(file_path)

    if data is None:
        return

    formatted_data = format_json(data)

    print("\n" + "-" * 45)
    print("FORMATTED JSON")
    print("-" * 45)
    print(formatted_data)

    save_json(formatted_data)


if __name__ == "__main__":
    main()