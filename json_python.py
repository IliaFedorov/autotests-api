import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))


json_data2 = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}
"""

parsed_data2 = json.loads(json_data2)

print(parsed_data2, type(parsed_data2))

print(parsed_data2['courses'])


data = {
  "name": "Мария",
  "age": 25,
  "is_student": True
}

json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r", encoding="utf8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)