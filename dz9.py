import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import date

conn = sqlite3.connect("v2222.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    temp INTEGER
);
''')

url = "https://www.gismeteo.ru/weather-katowice-3211/now/"
headers = {'User-Agent': 'Mozila/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

temp_div = soup.find("div", class_="now-weather")
temp_tag = temp_div.find("temperature-value")
try:
    temperature = int(temp_tag.get("value"))
    currdate = date.today().isoformat()
    res = cursor.execute("SELECT temp FROM weather where date = ?", [currdate])
    record = res.fetchone()
    if record is None:
        cursor.execute(
            "INSERT INTO weather (date, temp) VALUES (?, ?)",
            [currdate, temperature]
        )

        conn.commit()
        print("Дані додані:", currdate, temperature)
    else:
        print("Запис за сьогодні вже існує ", record[0],"C")
except:
    print("Parsing error")