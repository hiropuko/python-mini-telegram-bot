# Python Telegram-bot
Мини Telegram-бот на Python

````python

# library import / подключение библиотек
# pip install ccxt python-telegram-bot

import ccxt
import telegram
import asyncio
from config import TOKEN_KEY, CHAT_ID  # модуль KEY / ID


# переменные и значения
exchange = ccxt.binance()


bot = telegram.Bot(token=TOKEN_KEY)
chat_id = CHAT_ID


# Асинхронные операции без блокировки основного потока выполнения

async def send_btc_price():
    while True:
        # loop / цикл
        ticker = exchange.fetch_ticker('BTC/USDT')
        btc_price = ticker['last']
        await bot.send_message(chat_id=chat_id, text=f'BTC/USDT: {btc_price}')
        await asyncio.sleep(5)


asyncio.run(send_btc_price())  # Запуск асинхронной программы

````
