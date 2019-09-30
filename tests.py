#!/usr/bin/env python2
import requests
import json


def get_biens():
    url = 'http://127.0.0.1:5000/biens/Poissy'
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers = headers)
    print(response.text)


def create_user():
    url = 'http://127.0.0.1:5000/utilisateurs/new'
    headers = {"Content-Type": "application/json"}
    data = '{"nom":"Kabe", "prenom":"Lou", "annee":1918, "mois":4, "jour":2}'
    response = requests.post(url, data = data, headers = headers)
    print(response.text)


def update_user():
    url = 'http://127.0.0.1:5000/utilisateurs/update/2'
    headers = {"Content-Type": "application/json"}
    data = '{"nom":"Derle", "prenom":"Maud", "annee":1988, "mois":8, "jour":11}'
    response = requests.put(url, data = data, headers = headers)
    print(response.text)


def update_bien():
    url = 'http://127.0.0.1:5000/biens/update/2'
    headers = {"Content-Type": "application/json"}
    data = '{"nom": "Grand Appartement T3", "caracteristiques_pieces": "2 chambres, 1 cave", "description": "Tres bien situe dans la ville, ce T3 a tout pour vous satisfaire", "id": 2, "pieces": 3, "proprietaire_id": 1, "type": "appartement", "ville": "Conflans"}'
    response = requests.put(url, data = data, headers = headers)
    print(response.text)

print("Consulter les biens d'une ville particuliere")
get_biens()
print("--------------------------------------------\n")
print("Modification d'un bien")
update_bien()
print("--------------------------------------------\n")
print("Modification des informations personnelles")
update_user()
print("--------------------------------------------\n")
print("Ajout d'un utilisateur")
create_user()
