import json
import os 
import sys
import threading
from pycoingecko import CoinGeckoAPI
from threading import Timer
from dotenv import load_dotenv
import telebot

#metodo para obtener precios
def getprice():
    cg = CoinGeckoAPI()
    coinsprice = cg.get_price(ids='smooth-love-potion, axie-infinity', vs_currencies='usd', include_24h_vol=True, include_market_cap=True, result_limit=1000)
    print(coinsprice)

    #metodo para salvar precios en un json
    with  open('coins.json', 'w') as file:
        json.dump(coinsprice, file, indent= 3)

    #leyendo el archivo json
    coinsfile = open('coins.json', 'r')
    jsondata = coinsfile.read()

    #parser json
    obj = json.loads(jsondata)
    threading.Timer(1800,getprice).start()

    

#test solo para desarrollo
def printtest():
    precios = getprice()
    print(precios)
    threading.Timer(10,printtest)

imprime = printtest()

#telegram bot

load_dotenv()

API_KEY =  os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['slp'])
def slp(message):
    coinsfile = open('coins.json', 'r')
    jsondata = coinsfile.read()
    #parser json
    obj = json.loads(jsondata)
    slp = obj['smooth-love-potion']
    slp_price = slp['usd']
    slp_mcap = slp['usd_market_cap']
    image = 'https://assets.coingecko.com/coins/images/10366/small/SLP.png?1578640057'

    bot.reply_to(message,f"[.]({image})\nEl precio del slp es de: {slp_price}" + '\n' + f"El market cap del slp es de: {slp_mcap}" + '\n'  + '\n ** Grupo Axie Infinity by PortafolioF8N **', parse_mode='Markdown')

@bot.message_handler(commands=['axie'])
def axie(message):
    coinsfile = open('coins.json', 'r')
    jsondata = coinsfile.read()
    #parser json
    obj = json.loads(jsondata)
    axie = obj['axie-infinity']
    axie_price = axie['usd']
    axie_mcap = axie['usd_market_cap']
    image = 'https://assets.coingecko.com/coins/images/13029/small/axie_infinity_logo.png?1604471082'

    bot.reply_to(message,f"[.]({image})\n El precio del axie infinity es de: {axie_price}" + '\n' + f"El market cap del axie infinity es de: {axie_mcap}" + '\n'  + '\n ** Grupo Axie Infinity by PortafolioF8N **', parse_mode='Markdown')

bot.polling()