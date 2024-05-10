budget = float(input())
season = input()

destination = ""
type_of_place = ""

money_spend_coefficient = 0

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        type_of_place = "Camp"
        money_spend_coefficient = 0.3
    elif season == "winter":
        type_of_place = "Hotel"
        money_spend_coefficient = 0.7

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        type_of_place = "Camp"
        money_spend_coefficient = 0.4
    elif season == "winter":
        type_of_place = "Hotel"
        money_spend_coefficient = 0.8

elif budget > 1000:
    destination = "Europe"
    type_of_place = "Hotel"
    money_spend_coefficient = 0.9


print(f"Somewhere in {destination}")
print(f"{type_of_place} - {budget * money_spend_coefficient:.2f}")