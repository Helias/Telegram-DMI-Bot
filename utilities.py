# Coded By Adriano Ferraguto (Telegram: @adriano_effe)
# -*- coding: utf-8 -*-

import json
    
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
        output = "\nProfessore non trovato! :(\n\n"
    return output
