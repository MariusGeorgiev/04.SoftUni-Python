# prices of flowers
ROSE = 5
DALIA = 3.8
TULIP = 2.8
NARCISSUS = 3
GLADIOLUS = 2.5

type_flower = input()
num_flowers = int(input())
budget = int(input())

total_price = 0

if type_flower == "Roses":
    total_price = num_flowers * ROSE

    if num_flowers > 80:
        total_price *= 0.9

elif type_flower == "Dahlias":
    total_price = num_flowers * DALIA

    if num_flowers > 90:
        total_price *= 0.85

elif type_flower == "Tulips":
    total_price = num_flowers * TULIP

    if num_flowers > 80:
        total_price *= 0.85

elif type_flower == "Narcissus":
    total_price = num_flowers * NARCISSUS

    if num_flowers < 120:
        total_price *= 1.15

elif type_flower == "Gladiolus":
    total_price = num_flowers * GLADIOLUS

    if num_flowers < 80:
        total_price *= 1.2


if budget >= total_price:
    print(f"Hey, you have a great garden with {num_flowers} {type_flower} and {budget - total_price:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")