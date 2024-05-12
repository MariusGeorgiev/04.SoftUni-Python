age = int(input())
washing_machine = float(input())
toy = int(input())

money_from_even_birthday = 0
money_from_toys = 0
money_for_next_even = 10

for i in range(1, age+1):

    if i % 2 == 0:
        money_from_even_birthday += money_for_next_even
        money_for_next_even += 10
    else:
        money_from_toys += toy

money_from_even_birthday -= age // 2
total_money = money_from_toys + money_from_even_birthday


if total_money >= washing_machine:
    print(f"Yes! {total_money - washing_machine:.2f}")
elif total_money < washing_machine:
    print(f"No! {washing_machine - total_money:.2f}")