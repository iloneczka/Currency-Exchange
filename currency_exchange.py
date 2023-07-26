"""
Currency Exchange Rate Analysis

This application assists HSBC, the Swiss bank, in creating a program that reads and analyzes data from the National Bank of Poland (NBP) provided through the API. It retrieves and displays the value of a specified currency on a given date.

Usage:
- Run the program using the command prompt or terminal:
    ```
    python3 currency_exchange.py [currency_code] [date]
    ```
    If the command-line arguments `[currency_code]` and `[date]` are not provided, the program will prompt you to enter them.
"""

import requests
import sys
from dateutil.parser import parse

print("CURRENCY CALCULATOR")

if len(sys.argv) > 1:
    try:
        code = sys.argv[1].upper().strip()
        date = parse(sys.argv[2]).strftime("%Y-%m-%d")
    except IndexError:
        date = parse(input("Enter date: ")).strftime("%Y-%m-%d") 
else:
    code = input("Enter currency name: ").upper().strip()
    date = parse(input("Enter date: ")).strftime("%Y-%m-%d")

URL= f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"
# print(URL)

response = requests.get(URL)

if response.status_code == 404:
    print("No data available")
    sys.exit(2)

if response.status_code == 200:
    data = response.json()
    rate = data["rates"][0]["mid"]
    print(f'Exchange rate for {code.upper()} on date: {date} is: {rate}.')
