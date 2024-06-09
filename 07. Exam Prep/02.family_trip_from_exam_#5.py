budget = float(input())
nights = int(input())
price_of_nights = float(input())
percentage_add = int(input()) / 100

if nights > 7:
    price_of_nights *= 0.95

all_nights_price = price_of_nights * nights

additional_cost = budget * percentage_add

if budget >= (all_nights_price + additional_cost):
    print(f"Ivanovi will be left with {(budget - (all_nights_price + additional_cost)):.2f} leva after vacation.")
elif (all_nights_price + additional_cost) > budget:
    print(f"{((all_nights_price + additional_cost) - budget):.2f} leva needed.")