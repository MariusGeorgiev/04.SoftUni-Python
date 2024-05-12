nums = int(input())

first_sum = 0
second_sum = 0

for i in range(0, 2 * nums):

    num = int(input())

    if i < 2 * nums / 2:
        first_sum += num

    if i > 2 * nums / 2 - 1:
        second_sum += num


if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")

if first_sum < second_sum:
    print(f"No, diff = {second_sum - first_sum}")

if second_sum < first_sum:
    print(f"No, diff = {first_sum - second_sum}")

