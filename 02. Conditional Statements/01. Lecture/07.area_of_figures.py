import math

type_figure = input()

result = 0

if type_figure == 'square':
    length_side = float(input())
    result = length_side * length_side
elif type_figure == 'rectangle':
    length_side_one = float(input())
    length_side_two = float(input())
    result = length_side_one * length_side_two
elif type_figure == 'circle':
    radius_of_circle = float(input())
    result = radius_of_circle * math.pi * radius_of_circle
elif type_figure == 'triangle':
    length_side_one = float(input())
    length_height = float(input())
    result = length_height / 2 * length_side_one

print(f"{result:.3f}")