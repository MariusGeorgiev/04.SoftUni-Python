type_projection = input()
rows = int(input())
columns = int(input())

all_places = rows * columns

total_price = 0

if type_projection == "Premiere":
    total_price = all_places * 12
elif type_projection == "Normal":
    total_price = all_places * 7.5
elif type_projection == "Discount":
    total_price = all_places * 5

if total_price:
    print(f"{total_price:.2f} leva")