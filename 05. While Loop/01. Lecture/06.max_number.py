import sys

command = input()

max_num = -sys.maxsize

while command != "Stop":

    if int(command) > max_num:
        max_num = int(command)

    command = input()

print(max_num)