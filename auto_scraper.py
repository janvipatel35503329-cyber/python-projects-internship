import requests
from bs4 import BeautifulSoup
import time

print("📰 Simple Auto Scraper Started")

def scrape():
    url = "https://quotes.toscrape.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # first 3 quotes only (unique touch)
    quotes = soup.find_all("span", class_="text")[:3]

    print("\nLatest Quotes:")
    for q in quotes:
        print(q.text)

# run 2 times only (simple scheduler)
for i in range(2):
    scrape()
    print("\n⏳ Waiting...\n")
    time.sleep(5)