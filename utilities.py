# Codice scritto da Adriano Ferraguto (Telegram: @adriano_effe)
# -*- coding: utf-8 -*-

import json
import datetime
    
def getProfessori(input):
    with open("professori.json") as data_file:
        professori_data = json.load(data_file)
    output = ""
    i = 0
    risultati = 0
    while(professori_data[i]["ID"] != "-1") :
        if(input.lower() in professori_data[i]["Nome"].lower() or input.lower() in professori_data[i]["Cognome"].lower()):
            output += "Ruolo: " + professori_data[i]["Ruolo"] + "\n"
            output += "Cognome: " + professori_data[i]["Cognome"] + "\n"
            output += "Nome: " + professori_data[i]["Nome"] + "\n"
            output += "Indirizzo email : " + professori_data[i]["Email"] + "\n"
            output += "Sito web: " + professori_data[i]["Sito"] + "\n"
            output += "Scheda DMI: " + professori_data[i]["SchedaDMI"] + "\n\n"
            risultati += 1
        i += 1
    if (risultati == 0) :
        output = "\nNon sono stati trovati risultati :(\n\n"
    return output

def getLezioni(anno,semestre,giorno,corso):
    if (corso == "triennale"):
        with open("lezioni.json") as data_file:
            lezioni_data = json.load(data_file)
    elif (corso == "magistrale"):
        with open("mlezioni.json") as data_file:
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
        giorno = datetime.datetime.today().weekday()
    elif (inputArray[1] == "domani"):
		giorno = datetime.datetime.today().weekday()+1		
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


