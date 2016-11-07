# -*- coding: utf-8 -*-
import random
import requests
import os,sys

from utilities import *

import telegram.ext
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import sqlite3
conn = sqlite3.connect('DMI_DB.db')
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

gauth = GoogleAuth(settings_file=settings_file)
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
IDDrive='0B7-Gi4nb88hremEzWnh3QmN3ZlU'

#token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")
TOKEN = tokenconf      #Token of your telegram bot that you created from @BotFather, write it on token.conf
bot = telegram.Bot(TOKEN)

#debugging
#bot.sendMessage(chat_id=26349488, text="BOT ON")
#bot.sendMessage(chat_id=46806104,text="Sono online")

try:
	LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
	LAST_UPDATE_ID = 0

text = ""
try:
	while True:
		messageText = ""
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=2):
			if update.edited_message:
				LAST_UPDATE_ID = update_id + 1
				text=""
				break

			if update.callback_query:
				keyboard2=[[]];
				icona=""
				NumberRow=0
				NumberArray=0
				update_id = update.update_id


				if len(update.callback_query.data)<13:

					#conn.execute("DELETE FROM 'Chat_id_List'")
					ArrayValue=update['callback_query']['message']['text'].split(" ")
					try:
						if len(ArrayValue)==5:
							conn.execute("INSERT INTO 'Chat_id_List' VALUES ("+update.callback_query.data+",'"+ArrayValue[4]+"','"+ArrayValue[1]+"','"+ArrayValue[2]+"','"+ArrayValue[3]+"') ")
							bot.sendMessage(chat_id=update.callback_query.data,text= "🔓 La tua richiesta è stata accettata")
							bot.sendMessage(chat_id=-1001095167198,text=str(ArrayValue[1])+" "+str(ArrayValue[2]+str(" è stato inserito nel database")))

						elif len(ArrayValue)==4:
							conn.execute("INSERT INTO 'Chat_id_List'('Chat_id','Nome','Cognome','Email') VALUES ("+update.callback_query.data+",'"+ArrayValue[1]+"','"+ArrayValue[2]+"','"+ArrayValue[3]+"')")
							bot.sendMessage(chat_id=update.callback_query.data,text= "🔓 La tua richiesta è stata accettata")

						else:
							bot.sendMessage(chat_id=-1001095167198,text=str("ERRORE INSERIMENTO: ")+str(update['callback_query']['message']['text'])+" "+str(update['callback_query']['data']))
						conn.commit()
					except Exception as error:
						bot.sendMessage(chat_id=-1001095167198,text=str("ERRORE INSERIMENTO: ")+str(update['callback_query']['message']['text'])+" "+str(update['callback_query']['data']))



					LAST_UPDATE_ID = update_id + 1
					text = ""
					messageText = ""
					break

				else:
					if(os.fork()==0):
						gauth = GoogleAuth(settings_file=settings_file)
						gauth.CommandLineAuth()
						drive2 = GoogleDrive(gauth)
						bot2 = telegram.Bot(TOKEN)

						file1=drive2.CreateFile({'id':update.callback_query.data})
						if file1['mimeType']=="application/vnd.google-apps.folder":
							file_list2= drive2.ListFile({'q': "'"+file1['id']+"' in parents and trashed=false",'orderBy':'folder,title'}).GetList()
							for file2 in file_list2:

								fileN=""


								if file2['mimeType']=="application/vnd.google-apps.folder":
									if NumberRow>=1:
										keyboard2.append([InlineKeyboardButton("🗂 "+file2['title'], callback_data=file2['id'])])
										NumberRow=0
										NumberArray+=1
									else:
										keyboard2[NumberArray].append(InlineKeyboardButton("🗂 "+file2['title'], callback_data=file2['id']))
										NumberRow+=1
								else:
									if  ".pdf" in file2['title']:
										icona="📕 "
									elif ".doc" in file2['title'] or ".docx" in file2['title'] or ".txt" in file2['title'] :
										icona="📘 "
									elif ".jpg" in file2['title'] or ".png" in file2['title'] or ".gif" in  file2['title']:
										icona="📷 "
									elif ".rar" in file2['title'] or ".zip" in file2['title']:
										icona="🗄 "
									elif ".out" in file2['title'] or ".exe" in file2['title']:
										icona="⚙ "
									elif ".c" in file2['title'] or ".cpp" in file2['title'] or ".py" in file2['title'] or ".java" in file2['title'] or ".js" in file2['title'] or ".html" in file2['title'] or ".php" in file2['title']:
										icona="💻 "
									else:
										icona="📄 "
									if NumberRow>=1:
										keyboard2.append([InlineKeyboardButton(icona+file2['title'], callback_data=file2['id'])])
										NumberRow=0
										NumberArray+=1
									else:
										keyboard2[NumberArray].append(InlineKeyboardButton(icona+file2['title'], callback_data=file2['id']))
										NumberRow+=1

							if file1['parents'][0]['id'] != '0ADXK_Yx5406vUk9PVA':
								keyboard2.append([InlineKeyboardButton("🔙", callback_data=file1['parents'][0]['id'])])
							reply_markup3 = InlineKeyboardMarkup(keyboard2)
							bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'],text=file1['title']+":", reply_markup=reply_markup3)

						elif file1['mimeType'] == "application/vnd.google-apps.document":
							bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'], text="Impossibile scaricare questo file poichè esso è un google document, Andare sul seguente link")
							bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'], text=file1['exportLinks']['application/pdf'])

						else:
							try:
								fileD=drive2.CreateFile({'id':file1['id']})
								if int(fileD['fileSize']) < 5e+7:
									fileD.GetContentFile('file/'+file1['title'])
									fileS=file1['title']
									filex=open(str("file/"+fileS),"rb")
									bot2.sendDocument(chat_id=update['callback_query']['from_user']['id'], document=filex)
									os.remove(str("file/"+fileS))
								else:
									bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'], text="File troppo grande per il download diretto, scarica dal seguente link")
									bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'],text=fileD['alternateLink']) ##fileD['downloadUrl']
							except Exception as e:
								print str(e)
								bot2.sendMessage(chat_id=update['callback_query']['from_user']['id'],text="Impossibile scaricare questo file, contattare gli sviluppatori del bot")
								open("logs/errors.txt","a+").write(str(e)+str(fileD['title'])+"\n")

						sys.exit(0)
					else:
						LAST_UPDATE_ID = update_id + 1
						text = ""
						messageText = ""
						break
			else:
				text = update.message.text
				chat_id = update.message.chat.id
				update_id = update.update_id
				user = update.message.from_user.id


			if text != last_text and text != "":
				last_text = text

			originalText = text
			text = text.lower()

			if text.startswith('/'):
				if (text == '/help' or text == '/help@dmi_bot'): 											messageText = help_cmd()
				elif (text == '/rappresentanti' or text == '/rappresentanti@dmi_bot'): 						messageText = rapp_cmd()
				elif (text == '/rappresentanti_dmi' or text == '/rappresentanti_dmi@dmi_bot'): 				messageText = rapp_dmi_cmd()
				elif (text == '/rappresentanti_informatica' or text == '/rappresentanti_informatica@dmi_bot'): 	messageText = rapp_inf_cmd()
				elif (text == '/rappresentanti_matematica' or text == '/rappresentanti_matematica@dmi_bot'): 	messageText = rapp_mat_cmd()
				elif (text == '/sdidattica' or text == '/sdidattica@dmi_bot'): 								messageText = sdidattica_cmd()
				elif (text == '/sstudenti' or text == '/sstudenti@dmi_bot'):								messageText = sstudenti_cmd()
				elif (text == '/ersu' or text == '/ersu@dmi_bot'):										messageText = ersu_cmd()
				elif (text == '/ufficioersu' or text == '/ufficioersu@dmi_bot'):							messageText = ufficio_ersu_cmd()
				elif (text == '/urp' or text == '/urp@dmi_bot'):											messageText = urp_cmd()
				elif ('/prof' in text or '/prof@dmi_bot' in text):											messageText = prof_cmd(text)
				elif (text == '/esami' or text == '/esami@dmi_bot'):										messageText = "http://web.dmi.unict.it/Didattica/Laurea%20Triennale%20in%20Informatica%20L-31/Calendario%20dEsami"
				elif (text == '/mesami' or text == '/mesami@dmi_bot'):										messageText = 'http://web.dmi.unict.it/Didattica/Laurea%20Magistrale%20in%20Informatica%20LM-18/Calendario%20degli%20Esami'
				elif (text == '/aulario' or text == '/aulario@dmi_bot'):									messageText = 'http://aule.dmi.unict.it/aulario/roschedule.php'
				elif (text == '/mensa' or text == '/mensa@dmi_bot'):										messageText = mensa_cmd()
				elif (text == '/biblioteca' or text == '/biblioteca@dmi_bot'):								messageText = biblioteca_cmd()
				elif (text == '/cus' or text == '/cus@dmi_bot'):											messageText = cus_cmd()
				elif (text == '/smonta_portoni' or text == '/smonta_portoni@dmi_bot'):						messageText = smonta_portoni_cmd()
				elif (text == '/liste' or text == '/liste@dmi_bot'):
					img = 1
					picture = open("data/img/liste.png", "rb")
					messageText = "Liste e candidati"
				elif (text == '/contributors' or text == '/contributors@dmi_bot'):							messageText = contributors_cmd()
				elif ('/forum' in text or '/forum@dmi_bot' in text):										messageText = forum_cmd(text)
				elif (('/news' in text) and (chat_id == 26349488)):
					news = originalText.replace("/news ", "")
					messageText = "News Aggiornata!"
				elif ((text == '/spamnews' or text == '/spamnews@dmi_bot') and chat_id == 26349488 and news != "News"):
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
						messageText= "News disabilitate!"
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
				elif (text == '/drive' or text == '/drive@dmi_bot'):
					TestDB=0

					if chat_id < 0:
						bot.sendMessage(chat_id=chat_id,text="LA FUNZIONE /drive NON È AMMESSA NEI GRUPPI")
						LAST_UPDATE_ID = update_id + 1
						messageText=""
						text=""
						break
					else:
						for row in conn.execute("SELECT Chat_id FROM 'Chat_id_List' "):
							if row[0] == chat_id:
								TestDB=1;
						if TestDB==1:
							keyboard2=[[]];
							#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
							file_list = drive.ListFile({'q': "'"+IDDrive+"' in parents and trashed=false",'orderBy':'folder,title'}).GetList()
							NumberRow=0
							NumberArray=0
							for file1 in file_list:
								fileN=""
								if file1['mimeType']=="application/vnd.google-apps.folder":
									if NumberRow>=3:
										keyboard2.append([InlineKeyboardButton("🗂 "+file1['title'], callback_data=file1['id'])])
										NumberRow=0
										NumberArray+=1
									else:
										keyboard2[NumberArray].append(InlineKeyboardButton("🗂 "+file1['title'],callback_data=file1['id']))
										NumberRow+=1
								else:
									if NumberRow>=3:
										keyboard2.append([InlineKeyboardButton("📃 "+file1['title'], callback_data=file1['id'])])
										NumberRow=0
										NumberArray+=1
									else:
										keyboard2[NumberArray].append(InlineKeyboardButton("📃 "+file1['title'],callback_data=file1['id']))
										NumberRow+=1

							reply_markup3 = InlineKeyboardMarkup(keyboard2)
							bot.sendMessage(chat_id=chat_id,text="DMI UNICT - Appunti & Risorse:", reply_markup=reply_markup3)
							LAST_UPDATE_ID = update_id + 1
							messageText=""
							text=""
						else:
							bot.sendMessage(chat_id=chat_id,text="🔒 Non hai i permessi per utilizzare la funzione /drive,\n Utilizzare il comando /request <nome> <cognome> <e-mail> (il nome e il cognome devono essere scritti uniti Es: Di mauro -> Dimauro) ")
							LAST_UPDATE_ID = update_id + 1
							messageText=""
							text=""
							break

				elif ("/request" in text):


					if (chat_id>0):
						messageText="✉️ Richiesta inviata"
						keyboard=[[]]
						if (update['message']['from_user']['username']):
							username= update['message']['from_user']['username']
						else:
							username=""
						textSend=str(text)+" "+username
						keyboard.append([InlineKeyboardButton("Accetta", callback_data=str(chat_id))])
						reply_markup2=InlineKeyboardMarkup(keyboard)

						bot.sendMessage(chat_id=-1001095167198,text=textSend,reply_markup=reply_markup2)
						text=""
						break
					else:
						messageText="Non è possibile utilizzare /request in un gruppo"
						text=""
						break


				elif ("/adddb" in text and (chat_id==26349488 or chat_id==46806104)):
					ArrayValue=text.split(" ") #/add nome cognome e-mail username chatid
					if len(ArrayValue)==6:
						conn.execute("INSERT INTO 'Chat_id_List' VALUES ("+ArrayValue[5]+",'"+ArrayValue[4]+"','"+ArrayValue[1]+"','"+ArrayValue[2]+"','"+ArrayValue[3]+"') ")
						bot.sendMessage(chat_id=int(ArrayValue[5]),text= "🔓 La tua richiesta è stata accettata")
						conn.commit()
					elif len(ArrayValue)==5:
						conn.execute("INSERT INTO 'Chat_id_List'('Chat_id','Nome','Cognome','Email') VALUES ("+ArrayValue[4]+",'"+ArrayValue[1]+"','"+ArrayValue[2]+"','"+ArrayValue[3]+"')")
						bot.sendMessage(chat_id=int(ArrayValue[4]),text= "🔓 La tua richiesta è stata accettata")
						conn.commit()
					else:
						bot.sendMessage(chat_id=chat_id,text="/adddb <nome> <cognome> <e-mail> <username> <chat_id>")
					text=""
					LAST_UPDATE_ID = update_id + 1
					break


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
	bot.sendMessage(chat_id=-26349488,text=str(error))
	print str(error)
