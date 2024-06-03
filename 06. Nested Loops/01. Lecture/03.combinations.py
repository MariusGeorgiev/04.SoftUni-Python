input_number = int(input())

validNumbers = 0

for i in range(input_number + 1):
    for j in range(input_number + 1):
        for k in range(input_number + 1):
            if (i + j + k == input_number):
                validNumbers += 1

print(validNumbers)