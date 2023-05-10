# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.


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
