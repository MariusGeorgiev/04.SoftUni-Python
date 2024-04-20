length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

aquarium_volume = length * width * height

left_aquarium_liters = aquarium_volume - (aquarium_volume * percent)

print(left_aquarium_liters / 1000)
