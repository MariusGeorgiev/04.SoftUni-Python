numb = int(input())

points = numb

if points <= 100:
    points += 5
elif points <= 1000:
    points *= 1.2
elif points > 1000:
    points *= 1.1

if numb % 2 == 0:
    points += 1
elif numb % 10 == 5:
    points += 2

print(f"{points - numb:.1f}")
print(f"{points:.1f}")
