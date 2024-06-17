goal_for_the_day = int(input())

total_earn_money = 0

while True:
    type_of_service = input()

    if type_of_service == "closed":
        break

    for_who_and_type = input()

    if type_of_service == "haircut":
        if for_who_and_type == "mens":
            total_earn_money += 15
        elif for_who_and_type == "ladies":
            total_earn_money += 20
        elif for_who_and_type == "kids":
            total_earn_money += 10
    elif type_of_service == "color":
        if for_who_and_type == "touch up":
            total_earn_money += 20
        elif for_who_and_type == "full color":
            total_earn_money += 30

    if total_earn_money >= goal_for_the_day:
        break

if total_earn_money >= goal_for_the_day:
    print(f"You have reached your target for the day!")
elif goal_for_the_day > total_earn_money:
    print(f"Target not reached! You need {goal_for_the_day - total_earn_money}lv. more.")

print(f'Earned money: {total_earn_money}lv.')

