
import json

# Python Dictionary
x = {
    'name': "Usama",
    'gender': 'male',
    'dob': '08-Aug-2003',
    'age': '23',
    'mobile': '031417147714',
    'address': {
        'city': 'Karachi',
        'province': 'Sindh',
        'area': 'Saadi Town',
    }
}

# 1. Dictionary to JSON String
print("Original Dictionary:")
print(type(x))

y = json.dumps(x, indent=4)

print("\nJSON String:")
print(y)
print(type(y))


# 2. JSON String to Dictionary
z = json.loads(y)

print("\nConverted Back to Dictionary:")
print(z)
print(type(z))


# 3. Save Dictionary into JSON File
with open("data.json", "w") as file:
    json.dump(x, file, indent=4)

print("\nData successfully saved to JSON file!")


# 4. Read JSON File
with open("data.json", "r") as file:
    data = json.load(file)

print("\nData Read from JSON File:")
print(data)
print(type(data))
