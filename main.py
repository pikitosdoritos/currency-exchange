import requests
import time
import json

ENV = "prod"
ENV = "dev"

CURRENCY_API="https://api.monobank.ua/bank/currency"

CURRENCY_CODES = {
    "UAH": 980,
    "USD": 840,
    "EUR": 978,
    "GBP": 826,
    "JPY": 392,
}

def find_rate(rates, code_a, code_b):
    return rates.get((code_a, code_b))

def get_rates(env):
    if env == "dev":
        with open('rates.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    elif env == "prod":
        response = requests.get(CURRENCY_API)
        data = response.json()
    
    return {
        (item["currencyCodeA"], item["currencyCodeB"]): 
        item.get("rateBuy") or item.get("rateSell") or item.get("rateCross")
        for item in data
    }
            
rates = get_rates('dev')

usd_uah = find_rate(
    rates,
    CURRENCY_CODES["USD"],
    CURRENCY_CODES["UAH"]
)

print("USD → UAH:", usd_uah)