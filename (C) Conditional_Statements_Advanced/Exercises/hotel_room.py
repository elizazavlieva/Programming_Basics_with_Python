month = input()
nights = int(input())
total_price_studio = 0
total_price_apartment = 0
price_per_night_studio = 0
price_per_night_apartment = 0

#Logic

if 7 < nights <= 14 :
    if month == 'May' or month == 'October':
        price_per_night_apartment = 65
        price_per_night_studio = 50 * 0.95
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'June' or month == 'September':
        price_per_night_apartment = 68.70
        price_per_night_studio = 75.20
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'July' or month == 'August':
        price_per_night_apartment = 77
        price_per_night_studio = 76
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
elif nights > 14:
    if month == 'May' or month == 'October':
        price_per_night_apartment = 65 * 0.90
        price_per_night_studio = 50 * 0.70
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'June' or month == 'September':
        price_per_night_apartment = 68.70 * 0.90
        price_per_night_studio = 75.20 * 0.80
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'July' or month == 'August':
        price_per_night_apartment = 77 * 0.90
        price_per_night_studio = 76
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
elif nights <= 7:
    if month == 'May' or month == 'October':
        price_per_night_apartment = 65
        price_per_night_studio = 50
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'June' or month == 'September':
        price_per_night_apartment = 68.70
        price_per_night_studio = 75.20
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights
    elif month == 'July' or month == 'August':
        price_per_night_apartment = 77
        price_per_night_studio = 76
        total_price_apartment = price_per_night_apartment * nights
        total_price_studio = price_per_night_studio * nights

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')