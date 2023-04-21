import sys
import requests

# Get the number of Bitcoins to buy from the command-line argument
try:
    num_bitcoins = float(sys.argv[1])
except (IndexError, ValueError):
    print("Usage: python bitcoin.py <num_bitcoins>")
    sys.exit(1)

# Query the API for the current Bitcoin price
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    data = response.json()
    bitcoin_price = float(data['bpi']['USD']['rate'].replace(',', ''))
except (requests.RequestException, ValueError, KeyError):
    print("Failed to get Bitcoin price from API.")
    sys.exit(1)

# Calculate and output the cost of num_bitcoins in USD
cost_usd = num_bitcoins * bitcoin_price
print(f"{num_bitcoins:.8g} Bitcoins = ${cost_usd:,.4f} USD")
