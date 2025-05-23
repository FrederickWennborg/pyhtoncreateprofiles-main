import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    convert_csv_to_json("profiles1.csv", "profiles.json")
