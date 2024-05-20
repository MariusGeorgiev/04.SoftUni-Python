x = float(input())
y = float(input())
h = float(input())

DOOR = 1.2 * 2
WINDOWS = (1.5 * 1.5) * 2
front_and_back_side = (x * x) * 2
side_sides = (y * x) * 2
square_metres_walls = (front_and_back_side + side_sides) - DOOR - WINDOWS

roof_sides = (x * y) * 2
roof_frond_and_back = ((x * h) / 2) * 2
square_metres_roof = roof_sides + roof_frond_and_back

total_green_paint = square_metres_walls / 3.4
total_red_paint = square_metres_roof / 4.3

print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")