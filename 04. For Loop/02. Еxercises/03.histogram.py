n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    new_nums = int(input())
    if new_nums >= 800:
        p5 += 1
    elif 600 <= new_nums < 800:
        p4 += 1
    elif 400 <= new_nums < 600:
        p3 += 1
    elif 200 <= new_nums < 400:
        p2 += 1
    elif new_nums < 200:
        p1 += 1

print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")
