chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegeterian_menu_price = 8.15

delivery = 2.50

price = chicken_menu*chicken_menu_price + fish_menu_price*fish_menu + vegeterian_menu_price * vegeterian_menu
desert_price = price * 0.2

total_price = price + desert_price + delivery

print(round(total_price, 2))
