user_input = len("Enter Name: yu")

name = "Goke"
age = 10

formatted_string = f"I am {name}, age is {age}"

x = True
y = False

# print(type(age)) # check data type
# print(float(age)) # Type Casting

spaced_string = (
    "     this is fun      ".strip()
)  # Return a copy of the string with leading and trailing whitespace removed.
# print(spaced_string)

replaced_string = "I love Java!".lower().replace(
    "java", "Python"
)  # Return a copy with all occurrences of substring old replaced by new.


# if age > 10:
#     print("greater")

# elif age < 10:
#     print("less")

# else:
#     print("equal")


# for i in range(age):
#     print(i)


# password = ""
# while len(password) < 8:
#     password = input("Enter password (Min of 8 char): ")

# print("Password created successfully")


# PYTHON LIST OPERATIONS
my_list = [1, 4, 6, 1, 2, 3, 4, 5]

# my_list[2] = "hello"

# del my_list[4]
# my_list.remove(2)

# my_list.append(6)
# my_list.extend([7, 8, 9])
# my_list.insert(6, 12)

# my_list.sort()

# for i in my_list:
#     print(i)

# for i in range(len(my_list)):
#     print(my_list[i])

# i = 0

# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# LIST UNPACKING (DESTRUCTURING)
my_friends = ["wale", "tola", "halima", "funmi"]

first, second, *rest = my_friends
# print(first, second)
# print(rest)

# PYTHON DICTIONARIES (OBJECT)
student_data = {
    "name": "Goke",
    "age": 27,
    "grade": "A",
}

student_info = dict(
    name="Goke",
    age=27,
    is_student=True,
    # grade=[90, 96, 84],
)

# NESTED DICTIONARY
nested_data = {
    "person": {
        "name": "Goke",
        "age": 27,
        "grade": "A",
    }
}

# ACCESSING DICTS
# print(nested_data["person"])
# print(student_info.get("name"))
# print(student_info.get("person", "Does Not Exist"))

# ITERATING OVER DICTIONARIES

# for key in student_info:
#     print(f"{key}: {student_info[key]}")

# for key, value in student_info.items():
#     print(f"{key}: {value}")

# PYTHON DICTIONARIES OPERATIONS

# MODIFIYING
student_data["location"] = "London"  # add new field
student_data["name"] = "Goke Adekanye"  # modify existing field
student_data.update(
    {"name": "jvstblvck", "country": "UK"}
)  # update with new dictionary
student_data.update(name="jvstblvck", country="Britain")  # update with new dictionary
student_data.setdefault("gender", "male")  # set default

# DELETING
del student_data["gender"]
student_data.pop("country")
student_data.popitem()
student_data.clear()

# print(student_data)
# print(type(student_data))


# FUNCTIONS IN PYTHON
def func(x, y, z=[10, 20]):

    def inner():
        prodult = x * y * z[0]
        sum = x + y + z[1]
        return prodult, sum

    prodult, sum = inner()
    return prodult, sum


# prodult, sum = func(4, 3)
# prodult, sum = func(4, 3, [30, 40])

# print(prodult, sum)

# LAMBDA FUNCTIONS IN PYTHON (SIMPLIFIED FUNCION TYPE)
sum = lambda x, y: x + y


def parent(a, b, operation):
    return operation(a, b)


result = parent(16, 4, sum)

# print(result)

# MODULES IN PYTHON
import utils
from utils import increase_age as addup_age
from utils import *

# print(utils.print_name())
# print(addup_age(3))
# print(change_location("paris"))

# MODULES FROM PYTHON STANDARD LIB
from datetime import datetime

# current_date = datetime(year=2024, month=8, day=12, hour=3, minute=12, second=50)
current_date = datetime(year=2024, month=8, day=12, hour=3, minute=12, second=50)
# print(current_date.now())


# CLASS IN PYTHON
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"hello, {self.name}"


info = Person("Goke", 27)

# print(info.greet())


# OBJECT ORIENTED PROGRAMMING (OOP)
# INHERITANCE


# parent / base class
class Animal:
    def __init__(self, name):
        self.name = name

    def animal_info(self):
        return f"This is a {self.name}"


info = Animal("Goat")
print(info.animal_info())


# child / derived class
class mammal(Animal):
    def check(self):
        return "new mammal"


info2 = mammal("Cow")
print(info2.animal_info())
