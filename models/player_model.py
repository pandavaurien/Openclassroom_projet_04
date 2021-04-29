import time

from tinydb import TinyDB, Query
import pandas as pd

from controllers import main_control
from controllers import functions

player_database = TinyDB('models/players.json')


class Player:
 
    def __init__(self, last_name=None, first_name=None, birthdate=None, gender=None, ranking=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.home_menu_controller = main_control.HomeMenuController()

       # def __init__(self, player_infos=None):
    #     self.last_name = player_infos["Nom"]
    #     self.first_name = player_infos["Prénom"]
    #     self.birthdate = player_infos["Date de naissance"]
    #     self.gender = player_infos["Sexe"]
    #     self.ranking = player_infos["Classement"]
    
    def serialized_player(self):
        player_infos = {}
        player_infos['Nom'] = self.last_name
        player_infos['Prénom'] = self.first_name
        player_infos['Date de naissance'] = self.birthdate
        player_infos['Sexe'] = self.gender
        player_infos['Classement'] = self.ranking
        return player_infos

    def __repr__(self):
        return f"Nom :{self.last_name} Prénom : {self.first_name} classement :{self.ranking}"    

    def __str__(self):
        return f"""Nom :{self.last_name} Prénom : {self.first_name} classement :{self.ranking}"""
            
    def update_ranking(self):
        self.players_database = pd.read_json("models/players.json")
        print(self.players_database)
        print()
  
        valid_id = False
        while not valid_id:
            player_id = input("Entrer le numéro du joueur : ")
            if player_id.isdigit() and int(player_id) >=0 and int(player_id) <= len(self.players_database):
                valid_id = True
            else:
                print("Vous devez entrer le numéro correspondant au joueur")

        valid_ranking = False
        while not valid_ranking:
            new_ranking = input("Entrez le nouveau classement : ")
            if new_ranking.isdigit() and int(new_ranking) >=0:
                valid_ranking = True
            else:
                print("Vous devez entrer un nombre entier positif")
        player_to_modify = player_database.get(doc_id=int(player_id))
        
        # player_object = Player({player_to_modify})
        player_to_modify.update({"Classement" : new_ranking}) # Je ne fais pas d'instance ici, je modifie directement la base de données
        # print(player_to_modify)
        print(player_to_modify.__str__())
        time.sleep(2)
        self.home_menu_controller()   

    