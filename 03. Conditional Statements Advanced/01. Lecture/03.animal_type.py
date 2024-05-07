animal_type = input()

animal_class = "unknown"

if animal_type == "dog":
    animal_class = "mammal"
elif animal_type == "snake" or animal_type == "tortoise" or animal_type == "crocodile":
    animal_class = "reptile"

print(animal_class)