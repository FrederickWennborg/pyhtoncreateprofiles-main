import csv
import json
import os

def test_csv_column_count():
    with open("profiles1.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert len(headers) == 12

def test_csv_row_count():
    with open("profiles1.csv", newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))[1:]  # skip header
        assert len(reader) > 900

def test_json_row_count():
    with open("profiles.json", encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) > 900

def test_json_properties():
    with open("profiles.json", encoding='utf-8') as f:
        data = json.load(f)
    keys = data[0].keys()
    assert len(keys) == 12
    # optionally assert on specific fields like:
    assert "name" in keys
    assert "email" in keys
