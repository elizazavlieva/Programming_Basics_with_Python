mackerel_price = float(input())
sprat_price= float(input())
bonito_kg = float(input())
safrid_kg = float(input())
clam_kg = int(input())

bonito_price_kg = mackerel_price + (mackerel_price * 0.60)
bonito_price = bonito_kg * bonito_price_kg
safrid_price_kg = sprat_price + (sprat_price * 0.80)
safrid_price = safrid_price_kg * safrid_kg
clam_price = 7.50 * clam_kg

final_price = bonito_price + safrid_price + clam_price

print(f'{final_price:.2f}')
