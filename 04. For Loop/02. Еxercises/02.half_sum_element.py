n = int(input())

total = 0
max_number = 0

for i in range(0, n):
    new_num = int(input())
    total += new_num

    if i == 0:
        max_number = new_num

    if new_num >= max_number:
        max_number = new_num


if total / 2 == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
    exit()
else:
    total -= max_number

if total > max_number:
    print("No")
    print(f"Diff = {total - max_number}")
elif max_number > total:
    print("No")
    print(f"Diff = {max_number - total}")

