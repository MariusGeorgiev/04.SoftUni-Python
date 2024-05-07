age = float(input())
gender = input()

type_person = ""

if gender == "m":
    if age >= 16:
        type_person = "Mr."
    elif age < 16:
        type_person = "Master"

elif gender == "f":
    if age >= 16:
        type_person = "Ms."
    elif age < 16:
        type_person = "Miss"

print(type_person)