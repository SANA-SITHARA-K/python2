import requests
from  bs4 import BeautifulSoup
URL="https://books.toscrape.com/"
req=requests.get(URL)
source_code=req.content
soup=BeautifulSoup(source_code,'lxml')
print(soup)
articles=soup.find_all('article')
print(articles)
for article in articles:


    h3=article.find('h3')
    name=(h3.find('a')).text
    price=article.find('div',class_="product_price")
    price=price.find('p')
    price=price.text[1:]
    price=float(price)
    if price<50:
        with open('book.text','a') as file:
            file.write(name+ " : "+str(price)+"\n")
