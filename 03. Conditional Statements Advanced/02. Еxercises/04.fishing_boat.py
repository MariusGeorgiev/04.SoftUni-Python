budget = int(input())
season = input()
num_fishermen = int(input())

price_for_rent = 0

if season == "Spring":
    price_for_rent = 3000

elif season == "Summer":
    price_for_rent = 4200

elif season == "Autumn":
    price_for_rent = 4200

elif season == "Winter":
    price_for_rent = 2600


if num_fishermen <= 6:
    price_for_rent *= 0.9
elif 7 <= num_fishermen <= 11:
    price_for_rent *= 0.85
elif num_fishermen >= 12:
    price_for_rent *= 0.75

if num_fishermen % 2 == 0 and season != "Autumn":
    price_for_rent *= 0.95


if budget >= price_for_rent:
    print(f"Yes! You have {budget - price_for_rent:.2f} leva left.")
elif budget < price_for_rent:
    print(f"Not enough money! You need {price_for_rent - budget:.2f} leva.")




