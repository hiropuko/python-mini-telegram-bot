# Python mini Telegram-bot
Мини Telegram-бот на Python



````python
# library import / импорт библиотеки

import ccxt # pip install ccxt
import telegram # pip install python-telegram-bot
import asyncio
````
````python
# exchange object for interacting with the Binance API.
# объект exchange для взаимодействия с Binance API.

exchange = ccxt.binance()
````
````python
# an instance of the telegram.Bot class for messages in Telegram
# экземпляр класса telegram.Bot для сообщений в Telegram

bot = telegram.Bot(token='YOUR_TELEGRAM_TOKEN')
chat_id = 'YOUR_TELEGRAM_CHAT_ID'
````
````python
# function / функция

async def send_btc_price():
    while True:
    # loop / цикл
        ticker = exchange.fetch_ticker('BTC/USDT')
        btc_price = ticker['last']
        await bot.send_message(chat_id=chat_id, text=f'BTC/USDT: {btc_price}')
        await asyncio.sleep(5) # pause in seconds /  в секундах пауза
 ````
 ````python
 asyncio.run(send_btc_price()) # start function / запуск функции
 ````
