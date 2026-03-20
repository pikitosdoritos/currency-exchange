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

def find_rates(code_a, code_b):
    
    print(rates)

def get_rates(env):
    if env == "dev":
        with open('rates.json', 'r', encoding='utf-8') as f:
            data = f.read() 
    elif env == "prod":
        response = requests.get(CURRENCY_API)
        data = response.json()
    
    return data
            
rates = get_rates('dev') 

USD_UAH = find_rates(CURRENCY_CODES["UAH"], CURRENCY_CODES["USD"])