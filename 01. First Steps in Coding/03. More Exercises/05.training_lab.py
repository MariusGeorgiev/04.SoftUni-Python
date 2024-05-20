h = float(input())
w = float(input()) - 1

work_space_h = round(h // 1.2)
work_space_w = round(w // 0.7)

total_working_space = (work_space_h * work_space_w) - 3
print(total_working_space)

