import json

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

json_data = '''
{
    "users": [
        {
            "age": 22,
            "name": "john_USA"
        },
        {
            "age": 21,
            "name": "riya_NJ"
        },
        {
            "age": 20,
            "name": "Hari_NYC"
        }
       ]
}   
'''
py_data = json.loads(json_data)
print(type(py_data))
users = [User(user["name"],user["age"]) for user in py_data["users"]]

for user in users:
    print(user.get_name())



