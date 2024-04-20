PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEGETARIAN_MENU = 8.15
PRICE_DELIVERY = 2.50

number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegetarian_menus = int(input())

chickens_order_price = PRICE_CHICKEN_MENU * number_chicken_menus
fish_order_price = PRICE_FISH_MENU * number_fish_menus
vegetarians_order_price = PRICE_VEGETARIAN_MENU * number_vegetarian_menus

total_order_price = chickens_order_price + fish_order_price + vegetarians_order_price
desert_price = total_order_price * 0.20

print(total_order_price + desert_price + PRICE_DELIVERY)

