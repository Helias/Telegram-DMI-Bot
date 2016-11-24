# -*- coding: utf-8 -*-
import random
import requests
import os,sys
import re
from utilities import *

import telegram.ext
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, RegexHandler

import sqlite3
conn = sqlite3.connect('DMI_DB.db',check_same_thread=False)
#conn.execute("CREATE TABLE IF NOT EXISTS 'Chat_id_List' ('Chat_id' int(11) NOT NULL,'Username' text,'Nome' text NOT NULL,'Cognome' text NOT NULL,'Email' text NOT NULL);"  )

reload(sys)
sys.setdefaultencoding('utf8')

#chat_id log
logs = 1 #disable/enable chatid logs (1 enabled, 0 disabled)

#useful variables
news = "News"
img = 0
picture = ""
last_text = ""

settings_file = "config/settings.yaml"

#gauth = GoogleAuth(settings_file=settings_file)
#gauth.CommandLineAuth()
#gauth.LocalWebserverAuth()

#drive = GoogleDrive(gauth)


#token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")
TOKEN = tokenconf      		#Token of your telegram bot that you created from @BotFather, write it on token.conf
bot = telegram.Bot(TOKEN)

updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dp = updater.dispatcher


def main():

	#dp.add_handler(CommandHandler("help", help))
	dp.add_handler(RegexHandler('^(/Help|/help|/HELP)$',help))
	dp.add_handler(RegexHandler('^(/rappresentanti|/Rappresentanti|/RAPPRESENTANTI)$',rappresentanti))
	dp.add_handler(RegexHandler('^(/rappresentanti_dmi|/Rappresentanti_dmi|/RAPPRESENTANTI_DMI)$',rappresentanti_dmi))
	dp.add_handler(RegexHandler('^(/rappresentanti_informatica|/rappresentanti_informatica|/RAPPRESENTANTI_INFORMATICA)$',rappresentanti_info))
	dp.add_handler(RegexHandler('^(/rappresentanti_matematica|/rappresentanti_matematica|/RAPPRESENTANTI_MATEMATICA)$',rappresentanti_mate))
	#dp.add_handler(RegexHandler('^(/sdidattica|/Sdidattica|/SDIDATTICA)$',sdidattica))  
	dp.add_handler(RegexHandler('^(/sstudenti)$',sstudenti))
	dp.add_handler(RegexHandler('^(/ersu|/Ersu|/ERSU)$',ersu))
	dp.add_handler(RegexHandler('^(/ufficioersu|/Ufficioersu|/UFFICIOERSU)$',ufficioersu))
	dp.add_handler(RegexHandler('^(/urp|/Urp|/URP)$',urp))
	dp.add_handler(RegexHandler('^(/prof|/Prof|/PROF)$',prof))
	dp.add_handler(RegexHandler('^(/esami|/Esami|/ESAMI)$',esami))
	dp.add_handler(RegexHandler('^(/mesami|/Mesami|/MESAMI)$',mesami))
	dp.add_handler(RegexHandler('^(/aulario|/Aulario|/AULARIO)$',aulario))
	dp.add_handler(RegexHandler('^(/mensa|/Mensa|/MENSA)$',mensa))
	dp.add_handler(RegexHandler('^(/biblioteca|/Biblioteca|/BIBLIOTECA)$',biblioteca))
	dp.add_handler(RegexHandler('^(/cus|/Cus|/CUS)$',cus))
	dp.add_handler(RegexHandler('^(/smonta_portoni|/Smonta_portoni|/SMONTA_PORTONI)$',smonta_portoni))
	dp.add_handler(RegexHandler('^(/santino|/Santino|/SANTINO)$',santino))   #NN VA
	dp.add_handler(RegexHandler('^(/liste|/Liste|/LISTE)$',liste))
	dp.add_handler(RegexHandler('^(/contributors|/Contributors|/CONTRIBUTORS)$',contributors))
	dp.add_handler(RegexHandler('^(/forum|/Forum|/FORUM)$',forum_bot))
	#dp.add_handler(RegexHandler('^(/news|/News|/NEWS)$',news)) ## NN VA
	#dp.add_handler(RegexHandler('^(/spamnews|/Spamnews|/SPAMNEWS)$',spamnews)) ##NN VA
	#dp.add_handler(RegexHandler('^(/disablenews|/Disablenews|/DISABLENEWS)$',disablenews)) ##NN VA
	#dp.add_handler(RegexHandler('^(/enablenews|/Enablenews|/ENABLENEWS)$',enablenews)) ##NN VA
	dp.add_handler(RegexHandler('^(/drive|/Drive|/DRIVE)$',drive))
	dp.add_handler(RegexHandler('^(/adddb|/Adddb|/ADDDB)$',adddb))
	dp.add_handler(RegexHandler('^(/request|/Request|/REQUEST)$',request))
	dp.add_handler(CallbackQueryHandler(callback))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()
