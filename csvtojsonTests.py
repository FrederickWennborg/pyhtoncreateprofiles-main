import unittest
import csv
import json
import os

CSV_FILE = 'profiles1.csv'
JSON_FILE = 'profiles1.json'

class TestCSVtoJSON(unittest.TestCase):

    def test_csv_has_12_columns(self):
        with open(CSV_FILE, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(len(header), 12, "CSV should have exactly 12 columns")

    def test_csv_has_900_plus_rows(self):
        with open(CSV_FILE, newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            rows = list(reader)
            self.assertGreater(len(rows), 900, "CSV should have more than 900 rows")

    def test_json_has_all_expected_properties(self):
        with open(JSON_FILE) as f:
            data = json.load(f)
            sample = data[0]
            self.assertEqual(len(sample), 12, "Each JSON object should have 12 properties")

    def test_json_has_900_plus_rows(self):
        with open(JSON_FILE) as f:
            data = json.load(f)
            self.assertGreater(len(data), 900, "JSON should have more than 900 entries")

if __name__ == '__main__':
    unittest.main()
