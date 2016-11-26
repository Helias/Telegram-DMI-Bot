# -*- coding: utf-8 -*-
from utilities import *

conn = sqlite3.connect('DMI_DB.db',check_same_thread=False)
#conn.execute("CREATE TABLE IF NOT EXISTS 'Chat_id_List' ('Chat_id' int(11) NOT NULL,'Username' text,'Nome' text NOT NULL,'Cognome' text NOT NULL,'Email' text NOT NULL);"  )

reload(sys)
sys.setdefaultencoding('utf8')

updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dp = updater.dispatcher

def main():
	dp.add_handler(RegexHandler('^(/help|/Help|/HELP)$',help))
	dp.add_handler(RegexHandler('^(/rappresentanti|/Rappresentanti|/RAPPRESENTANTI)$',rappresentanti))
	dp.add_handler(RegexHandler('^(/rappresentanti_dmi|/Rappresentanti_dmi|/RAPPRESENTANTI_DMI)$',rappresentanti_dmi))
	dp.add_handler(RegexHandler('^(/rappresentanti_informatica|/rappresentanti_informatica|/RAPPRESENTANTI_INFORMATICA)$',rappresentanti_info))
	dp.add_handler(RegexHandler('^(/rappresentanti_matematica|/rappresentanti_matematica|/RAPPRESENTANTI_MATEMATICA)$',rappresentanti_mate))
	dp.add_handler(RegexHandler('/sdidattica',sdidattica))
	dp.add_handler(RegexHandler('/sstudenti',sstudenti))
	dp.add_handler(RegexHandler('^(/ersu|/Ersu|/ERSU)$',ersu))
	dp.add_handler(RegexHandler('^(/ufficioersu|/Ufficioersu|/UFFICIOERSU)$',ufficioersu))
	dp.add_handler(RegexHandler('^(/urp|/Urp|/URP)$',urp))
	dp.add_handler(RegexHandler('/prof',prof))
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
	dp.add_handler(RegexHandler('/forum',forum_bot))
	dp.add_handler(RegexHandler('/news',news_))
	dp.add_handler(RegexHandler('^(/spamnews|/Spamnews|/SPAMNEWS)$',spamnews))
	dp.add_handler(RegexHandler('^(/disablenews|/Disablenews|/DISABLENEWS)$',disablenews))
	dp.add_handler(RegexHandler('^(/enablenews|/Enablenews|/ENABLENEWS)$',enablenews))
	dp.add_handler(RegexHandler('^(/drive|/Drive|/DRIVE)$',drive))
	dp.add_handler(RegexHandler('/adddb',adddb))
	dp.add_handler(RegexHandler('/request',request))
	dp.add_handler(RegexHandler('/stat',stat))
	dp.add_handler(CallbackQueryHandler(callback))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()
