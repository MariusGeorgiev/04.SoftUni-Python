days = int(input())
num_hours = int(input())

total_price = 0

for i in range(1, days + 1):

    daily_price = 0

    for j in range(1, num_hours + 1):

        price = 1

        if i % 2 == 0 and j % 2 != 0:
            price = 2.50
        if i % 2 != 0 and j % 2 == 0:
            price = 1.25

        daily_price += price

    total_price += daily_price

    print(f"Day: {i} - {daily_price:.2f} leva")

print(f"Total: {total_price:.2f} leva")