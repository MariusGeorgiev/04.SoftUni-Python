import sys

command = input()

min_num = sys.maxsize

while command != "Stop":

    if int(command) < min_num:
        min_num = int(command)

    command = input()

print(min_num)