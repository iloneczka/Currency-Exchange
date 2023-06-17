"""
Currency Exchange Rate Analysis

This application assists HSBC, the Swiss bank, in creating a program that reads and analyzes data from the National Bank of Poland (NBP) provided through the API. It retrieves and displays the value of a specified currency on a given date.

The application allows HSBC to correctly issue invoices in foreign currencies in Poland. Regulations require converting amounts on such invoices to Polish złoty (PLN) using the NBP exchange rates from specific dates.

API Description: http://api.nbp.pl
1. Determine the URL format for retrieving the exchange rate of a specific currency on a given date.
2. Identify the required date format.
3. Understand how to modify the URL to receive the response in JSON format instead of XML.
4. Note that exchange rate tables are published only on business days. Refer to the documentation to understand what happens when requesting rates for weekends or public holidays.
5. The program accepts the currency and date as command-line arguments. However, if they are not provided, the user is prompted to enter these details using the input() function.

"""

import requests
import sys
from dateutil.parser import parse

print("KALKULATOR WALUT")

if len(sys.argv) > 1:
    try:
        code = sys.argv[1].upper().strip()
        date = parse(sys.argv[2]).strftime("%Y-%m-%d")
    except IndexError:
        date = parse(input("Podaj datę: ")).strftime("%Y-%m-%d") 
else:
    code = input("Podaj nazwę waluty: ").upper().strip()
    date = parse(input("Podaj datę: ")).strftime("%Y-%m-%d")

URL= f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"
# print(URL)

response = requests.get(URL)

if response.status_code == 404:
    print("Brak danych")
    sys.exit(2)

if response.status_code == 200:
    data = response.json()
    rate = data["rates"][0]["mid"]
    print(f'Kurs dla {code.upper()} na dzień: {date} wynosi: {rate}.')
