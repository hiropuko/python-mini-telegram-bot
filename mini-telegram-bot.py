import ccxt
import telegram
import asyncio

exchange = ccxt.binance()
bot = telegram.Bot(token='5813068415:AAH3306GmsNyYOPXiIVs3bR-TRiHoYVog7Q')
chat_id = '-1001884441347'

async def send_btc_price():
    while True:
        ticker = exchange.fetch_ticker('BTC/USDT')
        btc_price = ticker['last']
        await bot.send_message(chat_id=chat_id, text=f'BTC/USDT: {btc_price}')
        await asyncio.sleep(5)

asyncio.run(send_btc_price())
