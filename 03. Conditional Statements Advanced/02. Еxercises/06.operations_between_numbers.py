N1 = int(input())
N2 = int(input())
operator = input()

sum_after_operator = 0
even_or_odd = ""

if operator == "+":
    sum_after_operator = N1 + N2
elif operator == "-":
    sum_after_operator = N1 - N2
elif operator == "*":
    sum_after_operator = N1 * N2
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        sum_after_operator = N1 / N2

        print(f"{N1} {operator} {N2} = {sum_after_operator:.2f}")

elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        sum_after_operator = N1 % N2
        print(f"{N1} {operator} {N2} = {sum_after_operator}")

if sum_after_operator % 2 == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{N1} {operator} {N2} = {sum_after_operator} - {even_or_odd}")
