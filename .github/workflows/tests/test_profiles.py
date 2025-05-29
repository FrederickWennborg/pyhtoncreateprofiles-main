import csv
import json
#check if the csv file has 12 columns
def test_csv_12_columns():
    with open('profiles1.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) == 12, f"expected 12 columns got {len(header)}"


#check if the csv file has at least 900 rows
def test_csv_900_columns():
    with open('profiles1.csv', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))[1:] #exclude header
        assert len(reader) >= 900, f"Expected at least 900 rows got {len(reader)}"


#check if the json file has the expected keys
def test_json_correct_keys():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        expected_keys = [
            "Givenname", "Surname",
            "Streetaddress", "City", "Zipcode", "Country",
            "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
         ]
        for i, item in enumerate(data):
            for key in expected_keys:
                 assert key in item, f"Missing key: {key}"


#check if the json file has at least 900 rows
def test_json_900_rows():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) >= 900, f"Expected at least 900 rows got {len(data)}"
