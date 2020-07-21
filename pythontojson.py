import json

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = name + '@global.com'
        self.phone_number = '1234567889'
        self.profession = 'programmer'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def convert_to_dict_user(self):
        dict = {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone_number": self.phone_number,
            "profession":self.profession
                }
        return dict

users = [User("roma",16).convert_to_dict_user(), User("soni",17).convert_to_dict_user(),
        User("Jack",18).convert_to_dict_user(), User("avi",15).convert_to_dict_user(),
        User("Jary",18).convert_to_dict_user(), User("Myara",17).convert_to_dict_user()]

#json_data = json.dumps(users)
#print(json_data)

json_data = json.dumps(users, indent=2, sort_keys=True)
print(json_data)

