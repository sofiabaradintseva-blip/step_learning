import requests
from bs4 import BeautifulSoup
import sqlite3


class DataLinks:

    def __init__(self):
        self.conn = sqlite3.connect("v2222.db")
        self.cursor = self.conn.cursor()

    def init(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS links1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT
        ); 
        ''')

    def add_link(self, link):
        res = self.cursor.execute("SELECT 1 FROM links1 WHERE link = ?",[link])

        if res.fetchone() is not None:
            print("Link already exists")
            return

        try:
            self.cursor.execute("INSERT INTO links1 (link) VALUES (?)",[link])
            self.conn.commit()
            print("Link added")
        except Exception as e:
            print("Insert error:", e)

    def all_links(self):
        res = self.cursor.execute("SELECT link FROM links1")
        return res.fetchall()

    def interactive_insert(self):
        the_end = False
        while not the_end:
            new_link = input("Додайте посилання: ")
            self.add_link(new_link)
            the_end = input("Бажаєте ще додати (y/n)? ") == "n"


class Parser:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def find_h2(self, link):
        try:
            response = requests.get(link,headers=self.headers)
            soup = BeautifulSoup(response.text,"html.parser")
            h2_tags = soup.find_all("h2")
            return len(h2_tags)
        except Exception as e:
            print("Parse error:", e)
            return 0


db = DataLinks()
db.init()
db.interactive_insert()
parser = Parser()
for link in db.all_links():
    url = link[0]
    count = parser.find_h2(url)
    print(f"Посилання {url} має {count} тегів h2")