city = input()
sales = float(input())

commission = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5 / 100
    if 500 < sales <= 1000:
        commission = 7 / 100
    if 1000 < sales <= 10000:
        commission = 8 / 100
    if sales > 10000:
        commission = 12 / 100
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 / 100
    if 500 < sales <= 1000:
        commission = 7.5 / 100
    if 1000 < sales <= 10000:
        commission = 10 / 100
    if sales > 10000:
        commission = 13 / 100
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 / 100
    if 500 < sales <= 1000:
        commission = 8 / 100
    if 1000 < sales <= 10000:
        commission = 12 / 100
    if sales > 10000:
        commission = 14.5 / 100

city_s = city == "Plovdiv" or city == "Sofia" or city == "Varna"

if (sales < 0) or not city_s:
    print("error")
else:
    print(f"{sales * commission:.2f}")



