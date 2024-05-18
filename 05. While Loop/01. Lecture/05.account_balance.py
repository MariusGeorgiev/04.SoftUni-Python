data = input()
total = 0
while True:
    if data == "NoMoreMoney":
        print(f"Total: {total:.2f}")
        break

    if float(data) < 0:
        print("Invalid operation!")
        print(f"Total: {total:.2f}")
        break
    if float(data) > 0:
        total += float(data)
        print(f"Increase: {float(data):.2f}")

    data = input()

