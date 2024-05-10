ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days = int(input()) - 1
type_room = input()
grade = input()

price_for_all_night = 0

if days < 10:

    if type_room == "room for one person":
        price_for_all_night = days * ROOM
    elif type_room == "apartment":
        price_for_all_night = (days * APARTMENT) * 0.7
    elif type_room == "president apartment":
        price_for_all_night = (days * PRESIDENT_APARTMENT) * 0.9

elif 10 <= days <= 15:

    if type_room == "room for one person":
        price_for_all_night = days * ROOM
    elif type_room == "apartment":
        price_for_all_night = (days * APARTMENT) * 0.65
    elif type_room == "president apartment":
        price_for_all_night = (days * PRESIDENT_APARTMENT) * 0.85

elif days > 15:

    if type_room == "room for one person":
        price_for_all_night = days * ROOM
    elif type_room == "apartment":
        price_for_all_night = (days * APARTMENT) * 0.5
    elif type_room == "president apartment":
        price_for_all_night = (days * PRESIDENT_APARTMENT) * 0.8


if grade == "positive":
    price_for_all_night *= 1.25
elif grade == "negative":
    price_for_all_night *= 0.9

print(f"{price_for_all_night:.2f}")




