price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

EURO = 1.94

total_price_vegetables = price_kg_vegetables * total_kg_vegetables
total_price_fruits = price_kg_fruits * total_kg_fruits

total_sum = (total_price_vegetables + total_price_fruits) / EURO

print(f"{total_sum:.2f}")

