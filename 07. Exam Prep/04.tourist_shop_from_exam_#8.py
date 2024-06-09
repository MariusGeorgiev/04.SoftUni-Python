budget = float(input())

counter_buy_product = 0
counter_sum_all_buy_products = 0

while True:
    name_of_product = input()

    if name_of_product == "Stop":
        print(f"You bought {counter_buy_product} products for {counter_sum_all_buy_products:.2f} leva.")
        exit()

    price_of_product = float(input())
    counter_buy_product += 1

    if counter_buy_product % 3 == 0:
        price_of_product *= 0.5

    if price_of_product > budget:
        print("You don't have enough money!")
        print(f"You need {(price_of_product - budget):.2f} leva!")
        exit()

    counter_sum_all_buy_products += price_of_product
    budget -= price_of_product
