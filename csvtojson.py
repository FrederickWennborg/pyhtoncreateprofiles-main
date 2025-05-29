import csv
import json

csv_file = 'profiles1.csv'
json_file = 'profiles1.json'

def csv_to_json(csv_path, json_path):
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(json_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

        print(f"Successfully converted '{csv_path}' to '{json_path}'")

    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    csv_to_json(csv_file, json_file)
