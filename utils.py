student_data = {
    "name": "Goke Adekanye",
    "age": 27,
    "grade": "A",
}


def print_name():
    return student_data["name"]


def increase_age(value):
    new_age = student_data["age"] + value
    return new_age


def change_location(city):
    student_data.update({"location": city})
    return student_data
