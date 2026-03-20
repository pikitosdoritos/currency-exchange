import requests

CURRENCY_API="https://api.monobank.ua/bank/currency"

CURRENCY_CODES = {
    "UAH": 980,
    "USD": 840,
    "EUR": 978,
    "GBP": 826,
    "JPY": 392,
}

def get_currency():
    response = requests.get(CURRENCY_API)
    data = response.json()
    
    for item in data:        
        rate = item.get("rateBuy") or item.get("rateCross")
        
        if item['currencyCodeA'] == CURRENCY_CODES['USD']:
            print(f"USD: {rate}")
            
        elif item['currencyCodeA'] == CURRENCY_CODES['EUR']:
            print(f"EUR: {rate}")
            
        elif item['currencyCodeA'] == CURRENCY_CODES['GBP']:
            print(f"GBP: {rate}")
            
        elif item['currencyCodeA'] == CURRENCY_CODES['JPY']:
            print(f"JPY: {rate}")
            
get_currency()