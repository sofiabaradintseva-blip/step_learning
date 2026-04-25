import requests
from bs4 import BeautifulSoup

url = "https://privatbank.ua/obmin-valiut"
headers = {'User-Agent': 'Mozila/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

currencies = soup.find_all("div", class_="currency-pairs")
currency_dict = {}

for currency in currencies:
    name_tag = currency.find("div", class_="names")
    currency_name = name_tag.text.strip().split()[0]

    sale_tag = currency.find("div", class_="sale")
    if sale_tag:
        sale = sale_tag.text.strip()
    else:
        sale = None

    currency_dict[currency_name] = float(sale)
user_exit = False
while not user_exit:
    kurs = 1
    curr = 'UAH'
    try:
        user_choice = int(input("Яку валюту бажаєти придбати? (1 - EUR, 2 - USD, 3 - PLN) "))
    except:
        user_choice = -1
    if user_choice not in [1, 2, 3]:
        print("Помилка. Виберіть тільки 1, 2 або 3")
        continue
    try:
        count = int(input("Скільги гривні бажаєте конвертувати? "))
    except:
        count = 0
    if count <= 0:
        print("Помилка. Сума повинна бути білше 0")
        continue
    try:
        if user_choice == 1:
            kurs = currency_dict['EUR']
            curr = 'EUR'
            print("Обрана валюта: Євро")
        elif user_choice == 2:
            kurs = currency_dict['USD']
            curr = 'USD'
            print("Обрана валюта: Долари США")
        elif user_choice == 3:
            kurs = currency_dict['PLN']
            curr = 'PLN'
            print("Обрана валюта: Польский злотий")
    except:
        print("Помилка конвертації")
    print("Результат конвертації: ", round(count / kurs, 2), " ", curr, " по курсу: ", kurs)
    user_exit = input("Бажаєте продовжити (y/n)? ") == "n"
