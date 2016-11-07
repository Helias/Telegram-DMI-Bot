# -*- coding: utf-8 -*-
import json
import datetime
import urllib2
import re
import random
from bs4 import BeautifulSoup
from classes.StringParser import StringParser

def getProfessori(input):
    with open("data/json/professori.json") as data_file:
        professori_data = json.load(data_file)

    output = ""
    i = 0

    while(professori_data[i]["ID"] != "-1"):
        if (input == "/prof"):
	    return "La sintassi del comando è: /prof <nomeprofessore>"
	if len(input) < 3:
            return "Inserisci almeno 3 caratteri come nome/cognome del professore"
        elif (( input.lower() in professori_data[i]["Nome"].lower() ) or ( input.lower() in professori_data[i]["Cognome"].lower() )):
            output += "Ruolo: " + professori_data[i]["Ruolo"] + "\n"
            output += "Cognome: " + professori_data[i]["Cognome"] + "\n"
            output += "Nome: " + professori_data[i]["Nome"] + "\n"
            output += "Indirizzo email : " + professori_data[i]["Email"] + "\n"
            output += "Sito web: " + professori_data[i]["Sito"] + "\n"
            output += "Scheda DMI: " + professori_data[i]["SchedaDMI"] + "\n\n"
        i += 1
    if output == "":
        return "\nNon sono stati trovati risultati :(\n\n"

    return output

def getLezioni(anno,semestre,giorno,corso):
    if (corso == "triennale"):
        with open("data/json/lezioni.json") as data_file:
            lezioni_data = json.load(data_file)
    elif (corso == "magistrale"):
        with open("data/json/mlezioni.json") as data_file:
            lezioni_data = json.load(data_file)
    output = ""
    i = 0
    risultati = 0
    while(lezioni_data[i]["Nome"] != "nil") :
        if(lezioni_data[i]["GiornoSettimana"] == str(giorno) and lezioni_data[i]["Anno"] == anno and lezioni_data[i]["Semestre"] == semestre):
            output += "\nLezione di " + lezioni_data[i]["Nome"] + ", dalle ore " + lezioni_data[i]["OraInizio"] + " alle ore " + lezioni_data[i]["OraFine"] + ", in aula " + lezioni_data[i]["Aula"]
            risultati += 1
        i += 1
    if (risultati == 0):
        return "Nessuna lezione trovata per il giorno specificato"
    return output

def lezioni(input,corso):
    #Interpreta l'anno richiesto
    inputArray = input.split(' ')
    if (inputArray[0] == "primo"):
        anno = "1"
    elif (inputArray[0] == "secondo"):
        anno = "2"
    elif (inputArray[0] == "terzo"):
        anno = "3"
    else:
        return "Non ho capito la richiesta. Digita /help per maggiori info"
    #Interpreta il giorno della settimana
    if (len(inputArray) == 1 or inputArray[1] == "oggi"):
        giorno = datetime.datetime.today().weekday()+1
    elif (inputArray[1] == "domani"):
        giorno = datetime.datetime.today().weekday()+2
        if (giorno == 8):
            giorno = 1
    elif ("lun" in inputArray[1]):
        giorno = 1
    elif ("mar" in inputArray[1]):
        giorno = 2
    elif ("mer" in inputArray[1]):
        giorno = 3
    elif ("gio" in inputArray[1]):
        giorno = 4
    elif ("ven" in inputArray[1]):
        giorno = 5
    else:
        return "Non ho capito la richiesta. Digita /help per maggiori info"
    #Imposta il semestre corrente
    semestre = "1"
    #Chiama la funzione apposita con gli argomenti correttamente interpretati
    return getLezioni(anno,semestre,giorno,corso)


def forum(sezione):

    response = urllib2.urlopen("http://forum.informatica.unict.it/")
    html_doc = response.read()
    
    #print(html_doc)
    s = BeautifulSoup(html_doc, 'html.parser')
    s.prettify()
    dictionary = {}
    for rangeLimit,mainTable in enumerate(s.findAll("div", class_="tborder")):
        if(rangeLimit >= 3): #If che limita le sezioni a quelle interessate, evitando di stampare sottosezioni come "News" della categoria "Software"
            break
        for tdOfTable in mainTable.findAll("td", class_="windowbg3"):
            for spanUnder in tdOfTable.findAll("span", class_="smalltext"):
                for anchorTags in spanUnder.find_all('a'):
                    anchorTagsSplitted = anchorTags.string.split(",")
                    anchorTagsWithoutCFU = StringParser.removeCFU(anchorTagsSplitted[0])
                   
                    if(sezione == anchorTagsWithoutCFU.lower()):
                        dictionary[anchorTagsWithoutCFU.lower()] = anchorTags['href']
                        return dictionary

    return False


# Commands
CUSicon = {0 : "🏋",
	   1 : "⚽️",
	   2 : "🏀",
	   3 : "🏈",
	   4 : "🏐",
	   5 : "🏊",
}

def help_cmd():
	output = "@DMI_Bot risponde ai seguenti comandi: \n\n"
	output += "📖 /esami - /mesami - linka il calendario degli esami\n"
	output+= "🗓 /aulario - linka l\'aulario\n"
	output+= "👔 /prof <nome> - es. /prof Milici\n"
	output+= "🍽 /mensa - orario mensa\n"
	output+= "👥 /rappresentanti - elenco dei rappresentanti del DMI\n"
	output+= "📚 /biblioteca - orario biblioteca DMI\n"
	output+= CUSicon[random.randint(0,5)] + " /cus sede e contatti\n\n"
	output+= "Segreteria orari e contatti:\n"
	output+= "/sdidattica - segreteria didattica\n"
	output+= "/sstudenti - segreteria studenti\n"
	output+= "\nERSU orari e contatti\n"
	output+= "/ersu - sede centrale\n"
	output+= "/ufficioersu - (ufficio tesserini)\n"
	output+= "/urp - URP studenti\n\n"
	output+= "~Bot~\n"
	output+= "/disablenews \n"
	output+= "/enablenews\n"
	output+= "/contributors"
	return output

def rapp_cmd():
	output = "Usa uno dei seguenti comandi per mostrare i rispettivi rappresentanti\n"
	output += "/rappresentanti_dmi\n"
	output += "/rappresentanti_informatica\n"
	output += "/rappresentanti_matematica"
	return output

def rapp_dmi_cmd():
	output =  "Rappresentanti DMI\n"
	output += "Aliperti Vincenzo - @VAliperti\n"
	output += "Apa Marco - @MarcoApa\n"
	output += "Borzì Stefano - @Helias\n"
	output += "Costa Alberto - @knstrct\n"
	output += "Marroccia Marco - @MarcoLebon\n"
	output += "Mattia Ferdinando Alessandro - @AlessandroMattia\n"
	output += "Presente Fabrizio\n"
	output += "Petralia Luca- @lucapppla\n"
	output += "Rapisarda Simone - @CarlinoMalvagio\n"
	output += "Ricordo che per segnalare qualcosa a tutti i rappresentanti si può utilizzare l'email reportdmiunict@gmail.com"
	return output

def rapp_inf_cmd():
	output =  "Rappresentanti Inforamtica\n"
	output += "Aliperti Vincenzo - @VAliperti\n"
	output += "Apa Marco - @MarcoApa\n"
	output += "Borzì Stefano - @Helias\n"
	output += "Costa Alberto - @knstrct\n"
	output += "Giangreco Antonio - @Antonio0793\n"
	output += "Marroccia Marco - @MarcoLebon\n"
	return output

def rapp_mat_cmd():
	output =  "Rappresentanti Matematica\n"
	output += "Alessandro Massimiliano - @massi_94\n"
	output += "De Cristofaro Gaetano\n"
	output += "Pratissoli Mirco - @Mirko291194\n"
	output += "Sciuto Rita - @RitaSciuto"
	return output

def sditattica_cmd():
	output  = "Sede presso il Dipartimento di Matematica e Informatica (primo piano vicino al laboratorio) \n\n"
	output += "Sig.ra Cristina Mele\n"
	output += "📞 095/7337227\n"
	output += "✉️ cmele@dmi.unict.it\n\n"
	output += "🕑 Orari:\n"
	output += "Martedì dalle 10:30 alle 12:30\n"
	output += "Giovedì dalle 10:30 alle 12:30"
	return output

def sstudenti_cmd():
	output  = "Segreteria studenti\n"
	output += "Sede presso la Cittadella Universitaria (vicino la mensa)\n\n"
	output += "Via S. Sofia, 64 ed. 11 - 95125 Catania\n"
	output += "📞 095.7386103, 6119, 6109, 6125, 6129, 6123, 6122, 6106, 6107, 6121\n"
	output += "✉️ settore.scientifico@unict.it\n\n"
	output += "🕑 Orario invernale:\n"
	output += "Lunedi\': 10:00 - 12.30\n"
	output += "Martedi\': 10:00 -12:30 | 15:00 - 16:30\n"
	output += "Giovedi\': 10:00 - 12:30 | 15:00 - 16:30\n"
	output += "Venerdi\': 10:00 - 12:30"
	return output

def ersu_cmd():
	output  = "ERSU Catania - sede centrale\n"
	output += "Sede presso Via Etnea, 570\n\n"
	output += "📞 095/7517940 (ore 9:00/12:00)\n"
	output += "✉️ urp@ersucatania.gov.it\n\n"
	output += "🕑 Orari:\n"
	output += "Lunedì: 09:00 - 12:00\n"
	output += "Mercoledì: 15:30 - 18:00\n"
	output += "Venerdì: 09:00 - 12:00"
	return output

def ufficio_ersu_cmd():
	output  = "ERSU Catania - Ufficio Tesserini\n"
	output += "Sede della Cittadella (accanto l\'ingresso della Casa dello Studente)\n\n"
	output += "🕑 Orari:\n"
	output += "martedì-giovedì dalle 9.00 alle 12.30 \n\n"
	output += "UfficioErsu vicino la mensa Oberdan\n"
	output += "lunedì-mercoledì-venerdì dalle 09.00 alle 12.30 \n"
	output += "mercoledì 15:00 - 18.00:"
	return output

def urp_cmd():
	output = "URP Studenti\n"
	output += "Sede in Via A.di Sangiuliano, 44\n\n"
	output += "📞 800894327 (da fisso), 095 6139202/1/0\n"
	output += "✉️ urp-studenti@unict.it"
	return output

def prof_cmd(text):
	text = text.replace("@dmi_bot", "")
	text = text.replace("/prof ", "")
	output = getProfessori(text)
	return output

def mensa_cmd():
	output  = "🕑 Orario Mensa\n"
	output += "pranzo dalle ore 12,00 alle ore 14,30\n"
	output += "cena dalle ore 19,00 alle ore 21,30"
	return output

def biblioteca_cmd():
	output  = "Sala Lettura:\n"
	output += "lunedì - venerdì 08.00 - 19.00 \n\n"
	output += "Servizio Distribuzione: \n"
	output += "lunedì - giovedì 08.30 - 14.00 \n"
	output += "lunedì - giovedì 14.30 - 16.30 \n"
	output += "venerdì  08.30 - 13.30"
	return output

def cus_cmd():
	output = "CUS Catania\n"
	output += "Viale A. Doria n° 6  - 95125 Catania \n"
	output += "tel. 095336327- fax 095336478 \n"
	output += "info@cuscatania.it\n"
	output += "http://www.cuscatania.it/Contatti.aspx";
	return output

#Easter egg
def smonta_portoni_cmd():
	r = random.randint(0,13)
	if (r >= 0 and r <= 3):
		output = "$ sudo umount portoni"
	elif (r > 3 and r < 10):
		output = "@TkdAlex"
	elif (r == 11):
		output = "https://s16.postimg.org/5a6khjb5h/smonta_portoni.jpg"
	else:
		output = "https://s16.postimg.org/rz8117y9x/idraulico.jpg"
	return output

def contributors_cmd():
	output = "@Helias, @adriano_effe, @Veenz, @simone989\n"
	output +="https://github.com/Helias/telegram-dmi-bot"
	return output

def forum_cmd(text):
	text = text.replace("/forum ","")
	dictUrlSezioni = forum(text)
	if not (dictUrlSezioni == False):
		for titoli in dictUrlSezioni:
			output = StringParser.startsWithUpper(titoli)+": "+str(dictUrlSezioni[titoli])
	else:
		output = "La sezione non e' stata trovata."
	return output
