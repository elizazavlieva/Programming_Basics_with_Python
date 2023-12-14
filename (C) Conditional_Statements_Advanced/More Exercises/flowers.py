# Read user input

num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
feast = input()
total_flowers = num_chrysanthemums + num_tulips + num_roses
bouquet_price = 0
# Logic

if season == 'Spring' or season == 'Summer':
    bouquet_price = num_chrysanthemums * 2 + num_tulips * 2.50 + num_roses * 4.10
    if feast == 'Y':
        bouquet_price += (bouquet_price * 0.15)
    if season == 'Spring' and num_tulips > 7 :
        bouquet_price *= 0.95
elif season == 'Winter' or season == 'Autumn':
    bouquet_price = num_chrysanthemums * 3.75 + num_tulips * 4.15 + num_roses * 4.50
    if feast == 'Y':
        bouquet_price += bouquet_price * 0.15
    if num_roses >= 10 and season == 'Winter':
        bouquet_price *= 0.90
if total_flowers > 20:
    bouquet_price *= 0.80

bouquet_price += 2
# Print output
print(f'{bouquet_price:.2f}')