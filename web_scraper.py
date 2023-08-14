from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse

def ebay_scraper(url, document):
    title = document.select("h1.x-item-title__mainTitle")[0].text.strip()
    title = re.split(" - | AMD| Intel| Geforce| Nvidia| Windows", title)[0]
    
    find_text_by_parent = lambda parent, all_words: all_words[0].parent.find(parent).text
    
    words = document.select("div.x-price-primary")[0].text.strip()
    words = words.split("US ")[1].strip("$")
    
    true_price = float("".join(d for d in words if d != ","))
    
    return title, words, true_price
    
    
def newegg_scraper(url, document):
    title = document.select("h1.product-title")[0].text.strip()
    title = re.split(" - | AMD| Intel| Geforce| Nvidia| Windows", title)[0]
    
    find_text_by_parent = lambda parent, all_words: all_words[0].parent.find(parent).text
    
    words = document.select("li.price-current")[0].text.strip("$")
    true_price = float("".join(d for d in words if d != ","))
    
    return title, words, true_price
    
    
def main():
    url = input("Enter URL\n\n> ")
    domain = urlparse(url).netloc
    if domain == "www.ebay.com":
        choice = 1
    elif domain == "www.newegg.com":
        choice = 2
    else:
        print("Invalid URL")
        return
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    try:
        if choice == 1:
            title, formatted, true = ebay_scraper(url, doc)
        
        if choice == 2:
            title, formatted, true = newegg_scraper(url, doc)
    except Exception:
        return
    
    print(f'Price for "{title}" on {domain} is ${formatted}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit()