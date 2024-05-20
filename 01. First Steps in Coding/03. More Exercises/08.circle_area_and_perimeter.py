import math

r = float(input())

face = (r * r) * math.pi
perimeter = r * math.pi * 2

print(f"{face:.2f}")
print(f"{perimeter:.2f}")