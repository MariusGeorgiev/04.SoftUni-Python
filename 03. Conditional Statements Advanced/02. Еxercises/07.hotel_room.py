the_month = input()
num_nights = int(input())

price_all_nights_studio = 0
price_all_nights_apartment = 0

if the_month == "May" or the_month == "October":
    price_all_nights_studio = num_nights * 50
    price_all_nights_apartment = num_nights * 65
elif the_month == "June" or the_month == "September":
    price_all_nights_studio = num_nights * 75.2
    price_all_nights_apartment = num_nights * 68.7
elif the_month == "July" or the_month == "August":
    price_all_nights_studio = num_nights * 76
    price_all_nights_apartment = num_nights * 77

if num_nights > 14:
    price_all_nights_apartment *= 0.9

    if the_month == "May" or the_month == "October":
        price_all_nights_studio *= 0.7
    elif the_month == "June" or the_month == "September":
        price_all_nights_studio *= 0.8

elif num_nights > 7 and the_month == "May" or the_month == "October":
    price_all_nights_studio *= 0.95


print(f"Apartment: {price_all_nights_apartment:.2f} lv.")
print(f"Studio: {price_all_nights_studio:.2f} lv.")

