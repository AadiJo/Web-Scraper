from bs4 import BeautifulSoup
import requests
import re

def main():
    url = "NEWEGG URL HERE"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    
    words = doc.find_all(string=re.compile("$"))
    dollar = words[0].parent.find("strong")
    cents = words[0].parent.find("sup")
    print(dollar.text + cents.text)
        


if __name__ == '__main__':
    main()