from http.client import responses

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Ukraine"
headers = {'User-Agent': 'Mozila/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1").text
print("Назва статті: ", title)
paragraph = soup.find("p").text
print(paragraph)
paragraph = soup.find("p").text
print(paragraph)
sections = soup.find_all("h2")
for s in sections:
    print(s.text)

links = soup.find_all("a")
print("Number links: ", len(links))

for l in links:
    href = l.get("href")
    if href and href.startswith("/wiki/"):
        print("https://en.wikipedia.org" + href)

img = soup.find_all("img")
for i in img[:5]:
    print(i.get('src'))