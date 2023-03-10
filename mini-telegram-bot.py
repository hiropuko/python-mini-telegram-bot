import ccxt
import telegram
import asyncio

exchange = ccxt.binance() # 
bot = telegram.Bot(token='YOUR_TELEGRAM_TOKEN')
chat_id = 'YOUR_TELEGRAM_CHAT_ID'

async def send_btc_price():
    while True:
        ticker = exchange.fetch_ticker('BTC/USDT')
        btc_price = ticker['last']
        await bot.send_message(chat_id=chat_id, text=f'BTC/USDT: {btc_price}')
        await asyncio.sleep(5)

asyncio.run(send_btc_price())
