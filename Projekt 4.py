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

response= requests.get(URL)

if response.status_code == 404:
    print("Brak danych")
    sys.exit(2)

if response.status_code == 200:
    data = response.json()
    rate = data["rates"][0]["mid"]
    print(f'Kurs dla {code.upper()} na dzień: {date} wynosi: {rate}.')
