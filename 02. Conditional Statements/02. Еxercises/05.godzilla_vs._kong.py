budget_for_film = float(input())
statist = int(input())
price_for_dressing_one_statist = float(input())

decor_money = budget_for_film * 0.1

if statist > 150:
    price_for_dressing_one_statist *= 0.9

money_for_all_statist = statist * price_for_dressing_one_statist

all_money_neded = decor_money + money_for_all_statist

if all_money_neded > budget_for_film:
    print('Not enough money!')
    print(f"Wingard needs {all_money_neded - budget_for_film:.2f} leva more.")
elif budget_for_film >= all_money_neded:
    print("Action!")
    print(f"Wingard starts filming with {budget_for_film - all_money_neded:.2f} leva left.")
    