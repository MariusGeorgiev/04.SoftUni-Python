PACKING_PAPER_PRICE = 5.8
TEXTILE_PRICE = 7.2
GLUE_PRICE = 1.2

num_packing_paper = int(input())
num_textile = int(input())
liters_glue = float(input())
percentage_discount = int(input()) / 100

total_price_packing_paper = num_packing_paper * PACKING_PAPER_PRICE
total_price_textile = num_textile * TEXTILE_PRICE
total_price_glue = liters_glue * GLUE_PRICE

total_sum = total_price_packing_paper + total_price_textile + total_price_glue

total_after_discount = total_sum - (total_sum * percentage_discount)

print(f"{total_after_discount:.3f}")