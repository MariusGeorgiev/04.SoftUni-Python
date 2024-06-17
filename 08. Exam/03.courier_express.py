weight_package = float(input())
type_of_service = input()
distance = int(input())

price = 0

if weight_package < 1:
    price = 0.03
elif 1 <= weight_package < 10:
    price = 0.05
elif 10 <= weight_package < 40:
    price = 0.1
elif 40 <= weight_package < 90:
    price = 0.15
elif weight_package >= 90:
    price = 0.2

total_price = price * distance

price_up = 0

if type_of_service == "express":
    if weight_package < 1:
        price_up = (price * 0.8) * weight_package
    elif 1 <= weight_package < 10:
        price_up = (price * 0.4) * weight_package
    elif 10 <= weight_package < 40:
        price_up = (price * 0.05) * weight_package
    elif 40 <= weight_package < 90:
        price_up = (price * 0.02) * weight_package
    elif weight_package >= 90:
        price_up = (price * 0.01) * weight_package

if price_up > 0:
    total_price = total_price + (price_up * distance)


print(f"The delivery of your shipment with weight of {weight_package:.3f} kg. would cost {(total_price):.2f} lv.")

