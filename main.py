
import requests as requests
import pandas as pd
token = "cb01vviad3i0i2au9ppg"
allSymbol = ["AAPL","AMZN","NFLX","GOOGL","META"]
temp = -1000;
most_volatile_stock = {}
for symbol in allSymbol:
    base_url = "https://finnhub.io/api/v1/quote?"
    req = requests.get(base_url,params={'token':token,'symbol':symbol})
    stock_json = req.json()
    if stock_json['dp'] > temp:
        highest = stock_json['dp']
        temp = highest
        most_volatile_stock["stock_symbol"] = symbol
        most_volatile_stock["percentage_change"] = stock_json['dp']
        most_volatile_stock["current_price"] = stock_json['c']
        most_volatile_stock['last_close_price'] = stock_json['l']

df = pd.DataFrame.from_dict([most_volatile_stock])
df.to_csv(r'stock.csv', index=False, header=True)
