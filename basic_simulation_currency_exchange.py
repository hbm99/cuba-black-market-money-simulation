import json
import statistics
import random

days = int(input("Days to simulate: "))
days_to_get_money_exchange_trending = 15

# Opening JSON files
with open("eltoquedataEUR1000.json") as euro_file, open("eltoquedataMLC1000.json") as mlc_file, open("eltoquedataUSD1000.json") as usd_file:
    euro_data = json.load(euro_file)
    mlc_data = json.load(mlc_file)
    usd_data = json.load(usd_file)
    
def get_day_differences(currency_exchanges : list):
    day_differences = []
    for i in range(len(currency_exchanges) - days_to_get_money_exchange_trending + 1, 
                   len(currency_exchanges) - 1):
        day_differences.append(currency_exchanges[i + 1]['avg'] - currency_exchanges[i]['avg'])
    return day_differences

day_diffs_euro = get_day_differences(euro_data)
day_diffs_mlc = get_day_differences(mlc_data)
day_diffs_usd = get_day_differences(usd_data)

current_price_euro = euro_data[-1]['median'] + statistics.mean(day_diffs_euro)
current_price_mlc = mlc_data[-1]['median'] + statistics.mean(day_diffs_mlc)
current_price_usd = usd_data[-1]['median'] + statistics.mean(day_diffs_usd)

for i in range(days + 1):
    
    # Outside factor (not equal evaluation/deprecation)
    if random.randint(0, 6) == 5: # P = 1/5
        if random.choice([True, False]):
            current_price_euro += random.randint(-5, 5)
        if random.choice([True, False]):    
            current_price_mlc += random.randint(-5, 5)
        if random.choice([True, False]):
            current_price_usd += random.randint(-5, 5)
        
    # Outside factor (equal evaluation/deprecation)
    if random.randint(0, 9) == 2: # P = 1/10
        same_random = random.randint(-15, 15)
        current_price_euro += random.randint(-2, 2) + same_random
        current_price_mlc += random.randint(-2, 2) + same_random
        current_price_usd += random.randint(-2, 2) + same_random
        
    
    
    euro_offers = []
    for j in range(random.randint(300, 600)):
        euro_offers.append(current_price_euro + random.randint(-2, 6))
    current_price_euro = int(statistics.median(euro_offers))
    
    mlc_offers = []
    for j in range(random.randint(300, 600)):
        mlc_offers.append(current_price_mlc + random.randint(-2, 6))
    current_price_mlc = int(statistics.median(mlc_offers))
    
    usd_offers = []
    for j in range(random.randint(300, 600)):
        usd_offers.append(current_price_usd + random.randint(-2, 6))
    current_price_usd = int(statistics.median(usd_offers))

print("EUR : " + str(current_price_euro) + "\nMLC : " + str(current_price_mlc)
      + "\nUSD : " + str(current_price_usd))