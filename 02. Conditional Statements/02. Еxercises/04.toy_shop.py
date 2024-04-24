PUZZLE = 2.60
SPEAKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

price_of_excursion = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

all_toys = num_puzzles + num_dolls + num_bears + num_minions + num_trucks

price_puzzles = num_puzzles * PUZZLE
price_dolls = num_dolls * SPEAKING_DOLL
price_bears = num_bears * TEDDY_BEAR
price_minions = num_minions * MINION
price_trucks = num_trucks * TRUCK

price_all_toys = price_puzzles + price_dolls + price_bears + price_minions + price_trucks

if all_toys >= 50:
    price_all_toys *= 0.75

left_money_after_rent = price_all_toys * 0.9

if left_money_after_rent - price_of_excursion >= 0:
    print(f"Yes! {left_money_after_rent - price_of_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_excursion - left_money_after_rent:.2f} lv needed.")