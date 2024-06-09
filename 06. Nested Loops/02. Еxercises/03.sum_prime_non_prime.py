
sum_all_prime = 0
sum_all_non_prime = 0
current_number = ""

while True:
    current_number = input()
    if current_number == "stop":
        break

    current_number = int(current_number)

    if current_number < 0:
        print("Number is negative.")
        continue

    for number_counter in range(2, current_number + 1):
        if current_number % number_counter == 0 and current_number != number_counter:
            sum_all_non_prime += current_number
            break
        if current_number == number_counter:
            sum_all_prime += current_number

print(f"Sum of all prime numbers is: {sum_all_prime}")
print(f"Sum of all non prime numbers is: {sum_all_non_prime}")
