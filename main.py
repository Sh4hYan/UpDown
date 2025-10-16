from telethon import TelegramClient, events
from telethon.tl.custom.message import Message
from config import API_ID, API_HASH, BOT_TOKEN, TARGET_CHANNEL
import requests
import asyncio

bot = TelegramClient("Updown", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)
    
async def crypto_price(event: Message):
    while True:
        target_link = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,the-open-network,tron,dogecoin,notcoin,ethereum,solana,cardano,pepe,shiba-inu,x-empire,major,dogs,catizen&vs_currencies=usd"
        response = requests.get(target_link)
        if response.status_code != 200:
            await event.respond(f"Status Code Error: {response.status_code}")
            await asyncio.sleep(30)
            continue

        data = response.json()

        btc_price = f"{data['bitcoin']['usd']:,}"
        doge_price = f"{data['dogecoin']['usd']:,}"
        not_price = f"{data['notcoin']['usd']:,}"
        ton_price = f"{data['the-open-network']['usd']:,}"
        trx_price = f"{data['tron']['usd']:,}"
        eth_price = f"{data['ethereum']['usd']:,}"
        solana_price = f"{data['solana']['usd']:,}"
        cardano_price = f"{data['cardano']['usd']:,}"
        pepe_price = f"{data['pepe']['usd']:.8f}".rstrip('0').rstrip('.')
        shib_price = f"{data['shiba-inu']['usd']:.8f}".rstrip('0').rstrip('.')
        dogs_price = f"{data['dogs']['usd']:.8f}".rstrip('0').rstrip('.')
        x_price = f"{data['x-empire']['usd']:.8f}".rstrip('0').rstrip('.')
        major_price = f"{data['major']['usd']:.8f}".rstrip('0').rstrip('.')
        catizen_price = f"{data['catizen']['usd']:.8f}".rstrip('0').rstrip('.')
        
        crypto_price = (
        "💰 <b>The Crypto Prices:</b><br><br>\n\n"
        "---------------Popular---------------\n"
        f"👑 Bitcoin (BTC): <a href='https://www.coingecko.com/en/coins/bitcoin'><b>${btc_price}</b></a><br>\n"
        f"🐶 Dogecoin (DOGE): <a href='https://www.coingecko.com/en/coins/dogecoin'><b>${doge_price}</b></a><br>\n"
        f"🐕 Shiba Inu (SHIB): <a href='https://www.coingecko.com/en/coins/shiba-inu'><b>${shib_price}</b></a>\n"
        f"🔴 Tron (TRX): <a href='https://www.coingecko.com/en/coins/tron'><b>${trx_price}</b></a><br>\n"
        f"🔵 Toncoin (TON): <a href='https://www.coingecko.com/en/coins/the-open-network'><b>${ton_price}</b></a>\n"
        "---------------Airdrops---------------\n"
        f"🟡 Notcoin (NOT): <a href='https://www.coingecko.com/en/coins/notcoin'><b>${not_price}</b></a><br>\n"
        f"🐾 Dogs (DOGS): <a href='https://www.coingecko.com/en/coins/dogs'><b>${dogs_price}</b></a>\n"
        f"🪙 X-Empire (X): <a href='https://www.coingecko.com/en/coins/x-empire'><b>${x_price}</b></a><br>\n"
        f"🛡️ Major (MAJOR): <a href='https://www.coingecko.com/en/coins/major'><b>${major_price}</b></a>\n"
        f"🐱 Catizen (CATI): <a href='https://www.coingecko.com/en/coins/catizen'><b>${catizen_price}</b></a>\n"
        "---------------Watching---------------\n"
        f"🔱 Ethereum (ETH): <a href='https://www.coingecko.com/en/coins/ethereum'><b>${eth_price}</b></a>\n"
        f"🪩 Solana (SOL): <a href='https://www.coingecko.com/en/coins/solana'><b>${solana_price}</b></a>\n"
        f"🔮 Cardano (ADA): <a href='https://www.coingecko.com/en/coins/cardano'><b>${cardano_price}</b></a>\n"
        f"🦖 Pepe (PEPE): <a href='https://www.coingecko.com/en/coins/pepe'><b>${pepe_price}</b></a>\n"
        )

        await bot.send_message(TARGET_CHANNEL, crypto_price, parse_mode="html", link_preview=False)
        await asyncio.sleep(60)
        
@bot.on(events.NewMessage(pattern=r"(?i)/price$"))
async def crypto_price2(event: Message):
    await event.respond("📡 Start the activity...")
    asyncio.create_task(crypto_price(event))

@bot.on(events.NewMessage(pattern=r"(?i)/start$"))
async def starter(event: Message):
    await event.respond("✔️ I'm on!")
    
print("✅ Bot is activated...")
bot.run_until_disconnected()
