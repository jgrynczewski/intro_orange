import json


a_dict = {
    'a': 3,
    'b': 'awsdqwe',
    'c': [3, 4, 5]
}

# zapis do formatu json
with open('db.json', 'w+', encoding='utf-8') as f:
    json.dump(a_dict, f)

# odczyt z formatu json (z pliku - funkcja load biblioteki json)
with open('db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# dostajemy obiekty pythonowe
print(data)
print(data['c'])
print(data['c'][1])


# odczyt z formatu json (ze stringa - funkcja loads biblioteki json)
a_str = """
{"a": 3, "b": "awsdqwe", "c": [3, 4, 5]}
"""

data = json.loads(a_str)
print(data)
