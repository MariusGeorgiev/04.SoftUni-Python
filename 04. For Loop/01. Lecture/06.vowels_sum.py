text = input()

sum_of_all = 0

for char in text:
    if char == "a":
        sum_of_all += 1
    elif char == "e":
        sum_of_all += 2
    elif char == "i":
        sum_of_all += 3
    elif char == "o":
        sum_of_all += 4
    elif char == "u":
        sum_of_all += 5

print(sum_of_all)