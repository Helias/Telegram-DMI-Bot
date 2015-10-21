# -*- coding: utf-8 -*-
import telegram
from utilities import *

tokenconf = open('token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")

TOKEN = tokenconf      #Token of your telegram bot that you created from @BotFather, write it on token.conf

#chat_id log
logs = 1 #disable/enable chatid logs (1 enabled, 0 disabled)

news = "News"

bot = telegram.Bot(TOKEN)

#debugging
#bot.sendMessage(chat_id=26349488, text="BOT ON")

LAST_UPDATE_ID = bot.getUpdates()[-1].update_id

last_text = ""

try:
	while True:
		messageText = ""
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=2):
			text = update.message.text
			chat_id = update.message.chat.id
			update_id = update.update_id

		if text != last_text and text != "":
			last_text = text
		text = text.lower()
		if text.startswith('/'):
			if (text == '/help' or text == '/help@dmi_bot'):
				messageText = "@DMI_Bot risponde ai seguenti comandi (per la magistrale scrivete una \"m\" davanti ad ogni comando per esempio /mlezioni): \n/lezioni <anno> <giorno> (o /mlezioni per la magistrale) elenca le lezioni corrispondenti ai criteri scelti, <anno> deve essere \"primo\", \"secondo\" o \"terzo\", <giorno> deve essere \"oggi\", \"domani\", \"lunedì\", \"martedì\", \"mercoledì\", \"giovedì\" o \"venerdì\" - es. /lezioni secondo domani | /lezioni primo mercoledì \n/esami - /mesami - linka il calendario degli esami  \n/aulario - linka l\'aulario \n/prof <nome> - restituisce una lista dettagliata di professori i cui nomi e/o cognomi contengano <nome> - es. /prof Milici\n/mensa - orario mensa \n/biblioteca - orario biblioteca DMI \n\nSegreteria orari e contatti:\n/sdidattica - segreteria didattica \n/sstudenti - segreteria studenti \n ERSU orari e contatti \n/ersu - sede centrale\n/ufficioersu - (ufficio tesserini)\n\n/urp - URP studenti\n\n     Coded By @Helias && @adriano_effe"
			elif (text == '/sdidattica' or text == '/sdidattica@dmi_bot'):
				messageText = 'Sede presso il Dipartimento di Matematica e Informatica (primo piano vicino al laboratorio) \n\nSig.ra Cristina Mele Tel. 095/7337227\nEmail: cmele@dmi.unict.it\n\nOrari:\nLunedì dalle 15:00 alle 17:00\nGiovedì dalle 10:00 alle 12:00'
			elif (text == '/sstudenti' or text == '/sstudenti@dmi_bot'):
				messageText = 'Segreteria studenti\nSede presso la Cittadella Universitaria (vicino la mensa)\n\nVia S. Sofia, 64 ed. 11 - 95125 Catania\nTel. 095.7386103, 6119, 6109, 6125, 6129, 6123, 6122, 6106, 6107, 6121\nEmail: settore.scientifico@unict.it\n\nOrario invernale:\nLunedi\': 10:00 - 12.30\nMartedi\': 10:00 -12:30 | 15:00 - 16:30\nGiovedi\': 10:00 - 12:30 | 15:00 - 16:30\nVenerdi\': 10:00 - 12:30'
			elif (text == '/ersu' or text == '/ersu@dmi_bot'):
				messageText = 'ERSU Catania - sede centrale\nSede presso Via Etnea, 570\nTel. 095/7517940 (ore 9:00/12:00)\nEmail: urp@ersucatania.gov.it\n\nOrari:\nLunedì: 09:00 - 12:00\nMercoledì: 15:30 - 18:00\nVenerdì: 09:00 - 12:00'
			elif (text == '/ufficioersu' or text == '/ufficioersu@dmi_bot'):
				messageText = 'ERSU Catania - Ufficio Tesserini\nSede della Cittadella (accanto l\'ingresso della Casa dello Studente)\n\nOrari:\nLunedì: 09:00 - 12:30\nMartedì: 09:00 - 12:30\nMercoledì: 09:00 - 12:30 & 15:30 - 18:00\nGiovedì: 09:00 - 12:30\nVenerdì: 09:00 - 12:30'
			elif (text == '/urp' or text == '/urp@dmi_bot'):
				messageText = 'URP Studenti\nSede in Via A.di Sangiuliano, 44\n\nTel. 800894327 (da fisso), 095 6139202/1/0\nEmail: urp-studenti@unict.it'
			elif ('/professori' in text or '/professori@dmi_bot' in text or '/prof' in text or '/professore' in text or '/docente' in text or '/docenti' in text):
				text = text.replace("@dmi_bot", "")
				text = text.replace("/professori ", "")
				text = text.replace("/professore ", "")
				text = text.replace("/docenti ", "")
				text = text.replace("/docente ", "")
				text = text.replace("/prof ", "")
				messageText = getProfessori(text)
			elif ('/lezioni' in text):
				text = text.replace("@dmi_bot", "")
				text = text.replace("/lezioni ", "")
				messageText = lezioni(text,"triennale")
			elif ('/mlezioni' in text):
				text = text.replace("@dmi_bot", "")
				text = text.replace("/mlezioni ", "")
				messageText = lezioni(text,"magistrale")
			elif (text == '/esami' or text == '/esami@dmi_bot'):
				messageText = "http://web.dmi.unict.it/Didattica/Laurea%20Triennale%20in%20Informatica%20L-31/Calendario%20dEsami"
			elif (text == '/mesami' or text == '/mesami@dmi_bot'):
				messageText = 'http://web.dmi.unict.it/Didattica/Laurea%20Magistrale%20in%20Informatica%20LM-18/Calendario%20degli%20Esami'
			elif (text == '/aulario' or text == '/aulario@dmi_bot'):
				messageText = 'http://aule.dmi.unict.it/aulario/roschedule.php'
			elif (text == '/mensa'):
				messageText = "Orario Mensa\npranzo dalle ore 12,00 alle ore 14,30\ncena dalle ore 19,00 alle ore 21,30"
			elif (text == '/biblioteca'):
				messageText = "Sala Lettura:\nlunedì - venerdì 08.00 - 19.00 \n\nServizio Distribuzione: \nlunedì - giovedì 08.30 - 14.00 \nlunedì - giovedì 14.30 - 16.30 \nvenerdì  08.30 - 13.30"
			elif (('/news' in text) and (chat_id == 26349488 or chat_id == 26879677)):
				news = text.replace("/news ", "")
				messageText = "News Aggiornata!"
			elif (text == '/spamnews' and (chat_id == 26349488 or chat_id == 26879677) and news != "News"):
				chat_ids = open('log.txt', 'r').read()
				chat_ids = chat_ids.split("\n")
				for i in range((len(chat_ids)-1)):
					try:
						bot.sendMessage(chat_id=chat_ids[i], text=news)
					except Exception as error:
						open("errors.txt", "a+").write(str(error)+" "+str(chat_ids[i])+"\n")
				messageText = "News spammata!"

		if messageText != "":
			if logs != 0:
				log = open("log.txt", "a+")
				if not str(chat_id) in log.read():
					log.write(str(chat_id)+"\n")

			bot.sendMessage(chat_id=chat_id, text=messageText)
			LAST_UPDATE_ID = update_id + 1
			text = ""

except Exception as error:
	open("errors.txt", "a+").write(str(error)+"\n")

