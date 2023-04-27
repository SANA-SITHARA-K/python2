import requests
from  bs4 import BeautifulSoup
URL="https://books.toscrape.com/"
def scrape(URL):
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
return'books.txt'
import asyncio
from config import *
from telethon import TelegramClient,events

async def main():
    bot=await TelegramClient('session',API_ID,API_HASH).start(bot_token=BOT_TOKEN)

    async with bot:
        print("Logged in")
        @bot.on(events.NewMessage())
        async def handle_message(event):
            link=event.message.message
            file=scrape(link)
            user_id=event.sender.id
            await bot.send_file(user_id,file)
        await bot.run_until_disconnected()

asyncio.run(main())
