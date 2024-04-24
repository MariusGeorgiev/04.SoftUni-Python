budget = float(input())
num_gpus = int(input())
num_cpus = int(input())
num_rams = int(input())

GPU_PRICE = 250
CPU_PRICE = (num_gpus * GPU_PRICE) * 0.35
RAM_PRICE = (num_gpus * GPU_PRICE) * 0.10

needed_money = GPU_PRICE * num_gpus\
               + CPU_PRICE * num_cpus\
               + RAM_PRICE * num_rams

if num_gpus > num_cpus:
    needed_money *= 0.85

if budget >= needed_money:
    print(f"You have {budget - needed_money:.2f} leva left!")
elif budget < needed_money:
    print(f"Not enough money! You need {needed_money - budget:.2f} leva more!")