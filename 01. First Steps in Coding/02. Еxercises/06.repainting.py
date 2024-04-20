PRICE_SAFETY_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_PAINT_THINNER = 5.00
PRICE_BAGS = 0.40

needed_nylon = int(input()) + 2
need_paint = int(input())
needed_thinner = int(input())
working_hours = int(input())

total_price_nylon = needed_nylon * PRICE_SAFETY_NYLON
total_price_paint = (need_paint + (need_paint * 0.1)) * PRICE_PAINT
total_price_thinner = needed_thinner * PRICE_PAINT_THINNER

total = total_price_nylon + total_price_paint + total_price_thinner + PRICE_BAGS

payment_workers = (total * 0.3) * working_hours

print(total + payment_workers)

