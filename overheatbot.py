import logging
import requests
import os, time 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
from aiogram import Bot, Dispatcher, executor, md, types
import nltk
import OH
from OH import overheat

try:
    token = #ur token
    api = Bot(token = token, parse_mode=types.ParseMode.MARKDOWN)
    dp = Dispatcher(api)
    overheat = "100"
    overheat1 = "090"
    criticaloverheat = "200"
    sched = AsyncIOScheduler()
    print("Started!")


    if not os.path.exists("tempe.txt"):
        OH.overheat()
        oh = open("tempe.txt", encoding='utf-8').read().split(".")
    else:
        oh = open("tempe.txt", encoding='utf-8').read().split(".")

    if os.path.exists("id.txt"):
        usrid = open("id.txt", encoding='utf-8').read().split(" ")
        print(usrid)
    else:
        pass 

    def create_user(id):
        usrid = open('id.txt', "w", encoding='utf-8')
        id1 = usrid.write(str(id)) 

    def send_some_temps():
        r1 = oh[0]
        print(r1)
        if r1 > overheat1 < overheat:
            sm = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + usrid[0] + '&parse_mode=Markdown&text=' + "Overheat detected!" + " " + r1 + "Celsius"
            sr = requests.get(sm)
        else:
            sm = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + usrid[0] + '&parse_mode=Markdown&text=' + r1 + "Celsius"
            sr = requests.get(sm)

    @dp.message_handler(commands=['start'])
    async def heya(message: types.Message):
        id = message.chat.id
        create_user(id)
        usrid = open("id.txt", encoding='utf-8').read().split(" ")
        r = oh[1]
        print(r)
        if str(message.chat.id) in usrid:
            await message.reply(md.text(
                md.bold("Your CPU temps is: "),
                md.text(r + " " + "Celsius")
            ))
        else:
            await message.reply("Heya!You got registred")

    sched.add_job(send_some_temps, 'interval', minutes=10)
    sched.start()
    print('sched is started!')

    if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)

except(KeyboardInterrupt, SystemExit):
    sched.shutdown()