# -*- coding: utf-8 -*-
import telegram
import random
from utilities import *

#chat_id log
logs = 1 #disable/enable chatid logs (1 enabled, 0 disabled)

#useful variables
news = "News"
img = 0
picture = ""
last_text = ""

#token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")
TOKEN = tokenconf      #Token of your telegram bot that you created from @BotFather, write it on token.conf
bot = telegram.Bot(TOKEN)

#debugging
#bot.sendMessage(chat_id=26349488, text="BOT ON")

try:
	LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
	LAST_UPDATE_ID = 0

text = ""
try:
	while True:
		messageText = ""
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=2):
			text = update.message.text
			chat_id = update.message.chat.id
			update_id = update.update_id
			user = update.message.from_user.id

		if text != last_text and text != "":
			last_text = text

		originalText = text
		text = text.lower()

		if text.startswith('/'):
			if (text == '/help' or text == '/help@dmi_bot'):
				messageText  = "@DMI_Bot risponde ai seguenti comandi (per la magistrale scrivete una \"m\" davanti ad ogni comando per esempio /mesami): \n\n"
				messageText += "/esami - /mesami - linka il calendario degli esami\n"
				messageText += "/aulario - linka l\'aulario\n"
				messageText += "/prof <nome> - restituisce una lista dettagliata di professori i cui nomi e/o cognomi contengano <nome> - es. /prof Milici\n"
				messageText += "/mensa - orario mensa\n"
				messageText += "/rappresentanti - elenco dei rappresentanti del DMI\n"
				messageText += "/biblioteca - orario biblioteca DMI\n"
				messageText += "/cus sede e contatti\n\n"
				messageText += "Segreteria orari e contatti:\n"
				messageText += "/sdidattica - segreteria didattica\n"
				messageText += "/sstudenti - segreteria studenti\n"
				messageText += "\nERSU orari e contatti\n"
				messageText += "/ersu - sede centrale\n"
				messageText += "/ufficioersu - (ufficio tesserini)\n"
				messageText += "/urp - URP studenti\n\n"
				messageText += "~Bot~\n"
				messageText += "/disablenews \n"
				messageText += "/enablenews\n\nCoded By @Helias && @adriano_effe"
			elif (text == '/rappresentanti' or text == '/rappresentanti@dmi_bot'):
				messageText = "Usa uno dei seguenti comandi per mostrare i rispettivi rappresentanti\n"
				messageText += "/rappresentanti_dmi\n"
				messageText += "/rappresentanti_informatica\n"
				messageText += "/rappresentanti_matematica"
			elif (text == '/rappresentanti_dmi' or text == '/rappresentanti_dmi@dmi_bot'):
				messageText =  "Rappresentanti DMI\n"
				messageText += "Aliperti Vincenzo - @VAliperti\n"
				messageText += "Apa Marco - @MarcoApa\n"
				messageText += "Borzì Stefano - @Helias\n"
				messageText += "Costa Alberto - @knstrct\n"
				messageText += "Marroccia Marco - @MarcoLebon\n"
				messageText += "Mattia Ferdinando Alessandro - @Juzaz\n"
				messageText += "Presente Fabrizio\n"
				messageText += "Petralia Luca- @lucapppla\n"
				messageText += "Rapisarda Simone - @CarlinoMalvagio\n"
				messageText += "Ricordo che per segnalare qualcosa a tutti i rappresentanti si può utilizzare l'email reportdmiunict@gmail.com"
			elif (text == '/rappresentanti_informatica' or text == '/rappresentanti_informatica@dmi_bot'):
				messageText =  "Rappresentanti Inforamtica\n"
				messageText += "Aliperti Vincenzo - @VAliperti\n"
				messageText += "Apa Marco - @MarcoApa\n"
				messageText += "Borzì Stefano - @Helias\n"
				messageText += "Costa Alberto - @knstrct\n"
				messageText += "Giangreco Antonio - @Antonio0793\n"
				messageText += "Marroccia Marco - @MarcoLebon\n"
			elif (text == '/rappresentanti_matematica' or text == '/rappresentanti_matematica@dmi_bot'):
				messageText =  "Rappresentanti Matematica\n"
				messageText += "Alessandro Massimiliano - @massi_94\n"
				messageText += "De Cristofaro Gaetano\n"
				messageText += "Pratissoli Mirco - @Mirko291194\n"
				messageText += "Sciuto Rita - @RitaSciuto"
			elif (text == '/sdidattica' or text == '/sdidattica@dmi_bot'):
				messageText  = "Sede presso il Dipartimento di Matematica e Informatica (primo piano vicino al laboratorio) \n\n"
				messageText += "Sig.ra Cristina Mele Tel. 095/7337227\n"
				messageText += "Email: cmele@dmi.unict.it\n\n"
				messageText += "Orari:\n"
				messageText += "Martedì dalle 10:30 alle 12:30\n"
				messageText += "Giovedì dalle 10:30 alle 12:30"
			elif (text == '/sstudenti' or text == '/sstudenti@dmi_bot'):
				messageText  = "Segreteria studenti\n"
				messageText += "Sede presso la Cittadella Universitaria (vicino la mensa)\n\n"
				messageText += "Via S. Sofia, 64 ed. 11 - 95125 Catania\n"
				messageText += "Tel. 095.7386103, 6119, 6109, 6125, 6129, 6123, 6122, 6106, 6107, 6121\n"
				messageText += "Email: settore.scientifico@unict.it\n\n"
				messageText += "Orario invernale:\n"
				messageText += "Lunedi\': 10:00 - 12.30\n"
				messageText += "Martedi\': 10:00 -12:30 | 15:00 - 16:30\n"
				messageText += "Giovedi\': 10:00 - 12:30 | 15:00 - 16:30\n"
				messageText += "Venerdi\': 10:00 - 12:30"
			elif (text == '/ersu' or text == '/ersu@dmi_bot'):
				messageText  = "ERSU Catania - sede centrale\n"
				messageText += "Sede presso Via Etnea, 570\n"
				messageText += "Tel. 095/7517940 (ore 9:00/12:00)\n"
				messageText += "Email: urp@ersucatania.gov.it\n\n"
				messageText += "Orari:\n"
				messageText += "Lunedì: 09:00 - 12:00\n"
				messageText += "Mercoledì: 15:30 - 18:00\n"
				messageText += "Venerdì: 09:00 - 12:00"
			elif (text == '/ufficioersu' or text == '/ufficioersu@dmi_bot'):
				messageText  = "ERSU Catania - Ufficio Tesserini\n"
				messageText += "Sede della Cittadella (accanto l\'ingresso della Casa dello Studente)\n\n"
				messageText += "Orari:\n"
				messageText += "martedì-giovedì dalle 9.00 alle 12.30 \n\n"
				messageText += "UfficioErsu vicino la mensa Oberdan\n"
				messageText += "lunedì-mercoledì-venerdì dalle 09.00 alle 12.30 \n"
				messageText += "mercoledì 15:00 - 18.00:"
			elif (text == '/urp' or text == '/urp@dmi_bot'):
				messageText = "URP Studenti\n"
				messageText += "Sede in Via A.di Sangiuliano, 44\n\n"
				messageText += "Tel. 800894327 (da fisso), 095 6139202/1/0\n"
				messageText += "Email: urp-studenti@unict.it"
			elif ('/professori' in text or '/professori@dmi_bot' in text or '/prof' in text or '/professore' in text or '/docente' in text or '/docenti' in text):
				text = text.replace("@dmi_bot", "")
				text = text.replace("/professori ", "")
				text = text.replace("/professore ", "")
				text = text.replace("/docenti ", "")
				text = text.replace("/docente ", "")
				text = text.replace("/prof ", "")
				messageText = getProfessori(text)
			elif (text == '/esami' or text == '/esami@dmi_bot'):
				messageText = "http://web.dmi.unict.it/Didattica/Laurea%20Triennale%20in%20Informatica%20L-31/Calendario%20dEsami"
			elif (text == '/mesami' or text == '/mesami@dmi_bot'):
				messageText = 'http://web.dmi.unict.it/Didattica/Laurea%20Magistrale%20in%20Informatica%20LM-18/Calendario%20degli%20Esami'
			elif (text == '/aulario' or text == '/aulario@dmi_bot'):
				messageText = 'http://aule.dmi.unict.it/aulario/roschedule.php'
			elif (text == '/mensa' or text == '/mensa@dmi_bot'):
				messageText  = "Orario Mensa\n"
				messageText += "pranzo dalle ore 12,00 alle ore 14,30\n"
				messageText += "cena dalle ore 19,00 alle ore 21,30"
			elif (text == '/biblioteca' or text == '/biblioteca@dmi_bot'):
				messageText  = "Sala Lettura:\n"
				messageText += "lunedì - venerdì 08.00 - 19.00 \n\n"
				messageText += "Servizio Distribuzione: \n"
				messageText += "lunedì - giovedì 08.30 - 14.00 \n"
				messageText += "lunedì - giovedì 14.30 - 16.30 \n"
				messageText += "venerdì  08.30 - 13.30"
			elif (text == '/cus' or text == '/cus@dmi_bot'):
				messageText = "CUS Catania\n"
				messageText += "Viale A. Doria n° 6  - 95125 Catania \n"
				messageText += "tel. 095336327- fax 095336478 \n"
				messageText += "info@cuscatania.it\n"
				messageText += "http://www.cuscatania.it/Contatti.aspx";
			elif (text == '/liste' or text == '/liste@dmi_bot'):
				img = 1
				picture = open("data/img/liste.png", "rb")
				messageText = "Liste e candidati"
			elif (('/news' in text) and (chat_id == 26349488)):
				news = originalText.replace("/news ", "")
				messageText = "News Aggiornata!"
			elif (text == '/spamnews' and chat_id == 26349488 and news != "News"):
				chat_ids = open('logs/log.txt', 'r').read()
				chat_ids = chat_ids.split("\n")
				for i in range((len(chat_ids)-1)):
					try:
						if not "+" in chat_ids[i]:
							bot.sendMessage(chat_id=chat_ids[i], text=news)
					except Exception as error:
						open("logs/errors.txt", "a+").write(str(error)+" "+str(chat_ids[i])+"\n")
				messageText = "News spammata!"
			elif (text == '/disablenews' or text == '/disablenews@dmi_bot'):
				chat_ids = open('logs/log.txt', 'r').read()
				if not ("+"+str(chat_id)) in chat_ids:
					chat_ids = chat_ids.replace(str(chat_id), "+"+str(chat_id))
					messageText = "News disabilitate!"
					open('logs/log.txt', 'w').write(chat_ids)
				else:
					messageText = "News già disabilitate!"
			elif (text == '/enablenews' or text == '/enablenews@dmi_bot'):
				chat_ids = open('logs/log.txt', 'r').read()
				if ("+"+str(chat_id)) in chat_ids:
					chat_ids = chat_ids.replace("+"+str(chat_id), str(chat_id))
					messageText = "News abilitate!"
					open('logs/log.txt', 'w').write(chat_ids)
				else:
					messageText = "News già abilitate!"
			elif ('/forum' in text):
				text = text.replace("/forum ","")
				dictUrlSezioni = forum(text)
				if not (dictUrlSezioni == False):
					for titoli in dictUrlSezioni:
						messageText = StringParser.startsWithUpper(titoli)+": "+str(dictUrlSezioni[titoli])
				else:
					messageText = "La sezione non e' stata trovata."


		if messageText != "":
			if logs != 0:
				log = open("logs/log.txt", "a+")
				if not str(chat_id) in log.read():
					log.write(str(chat_id)+"\n")
			if (img == 1):
				bot.sendPhoto(chat_id=chat_id, photo=picture)
				img = 0
				picture = ""
			else:
				bot.sendMessage(chat_id=chat_id, text=messageText)
			LAST_UPDATE_ID = update_id + 1
			text = ""
except Exception as error:
	open("logs/errors.txt","a+").write(str(error)+"\n")
