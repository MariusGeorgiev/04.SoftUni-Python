need_money = float(input())
money_left = float(input())

count_days_spend = 0
count_days = 0

while True:
    if count_days_spend == 5:
        print(f"You can't save the money.")
        print(count_days)
        break

    type_command = input()
    money_sum = float(input())

    count_days += 1

    if type_command == "spend":
        money_left -= money_sum
        count_days_spend += 1
        if money_left < 0:
            money_left = 0

    if type_command == "save":
        money_left += money_sum
        count_days_spend = 0

    if money_left >= need_money:
        print(f"You saved the money for {count_days} days.")
        break

