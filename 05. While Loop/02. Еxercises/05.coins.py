change = float(input())

count_monet = 0

while True:

    # change = round(change, 2)

    if change >= 2:
        count_monet += 1
        change = round(change - 2, 2)
    elif change >= 1:
        count_monet += 1
        change = round(change - 1, 2)
    elif change >= 0.50:
        count_monet += 1
        change = round(change - 0.50, 2)
    elif change >= 0.20:
        count_monet += 1
        change = round(change - 0.20, 2)
    elif change >= 0.10:
        count_monet += 1
        change = round(change - 0.10, 2)
    elif change >= 0.05:
        count_monet += 1
        change = round(change - 0.05, 2)
    elif change >= 0.02:
        count_monet += 1
        change = round(change - 0.02, 2)
    elif change == 0.01:
        count_monet += 1
        change = round(change - 0.01, 2)

    if change < 0.01:
        break

print(count_monet)
