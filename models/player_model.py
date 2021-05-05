import time

from tinydb import TinyDB, Query
import pandas as pd

from controllers import main_control
from controllers import player_controller

player_database = TinyDB('models/players.json')


class Player:
 
    def __init__(self, last_name=None, first_name=None, birthdate=None, gender=None, ranking=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.home_menu_controller = main_control.HomeMenuController()
        self.tournament_score = 0

    def serialized(self):
        player_infos = {}
        player_infos['Nom'] = self.last_name
        player_infos['Prénom'] = self.first_name
        player_infos['Date de naissance'] = self.birthdate
        player_infos['Sexe'] = self.gender
        player_infos['Classement'] = self.ranking
        return player_infos

    def unserialized(self, serialized_player):
        last_name = serialized_player["Nom"]
        first_name = serialized_player["Prénom"]
        birthdate = serialized_player["Date de naissance"]
        gender = serialized_player["Sexe"]
        ranking = serialized_player["Classement"]
        return Player(last_name, first_name, birthdate, gender, ranking)

    def __str__(self):
        return f"{self.last_name} {self.first_name}, classement : {self.ranking}"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"
        
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
        player_to_modify["Classement"] = new_ranking
        
        print(f"{player_to_modify['Nom']} {player_to_modify['Prénom']} \n"
            f"Nouveau classement : {player_to_modify['Classement']}")
        time.sleep(2.5)
        self.home_menu_controller() 

    def add_to_database(self, player_values):
        player = Player(player_values[0],
                        player_values[1],
                        player_values[2],
                        player_values[3],
                        player_values[4]
                        )
        player_database.insert(player.serialized())
        time.sleep(2)

      
    