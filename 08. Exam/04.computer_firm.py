num_pcs = int(input())

total_sales = 0
total_rating = 0
for i in range(num_pcs):
    data = int(input())

    rating = data % 10
    possible_sales = int(str(data)[:2])

    if rating == 2:
        possible_sales = 0
    elif rating == 3:
        possible_sales *= 0.5
    elif rating == 4:
        possible_sales *= 0.7
    elif rating == 5:
        possible_sales *= 0.85

    if 2 <= rating <= 6:
        total_sales += possible_sales
        total_rating += rating

print(f"{total_sales:.2f}")
print(f"{(total_rating / num_pcs):.2f}")


