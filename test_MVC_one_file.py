# coding: utf-8

"""docstring"""
from tinydb import TinyDB, Query
player_database = TinyDB('players.json')

class ViewAddPlayer:
    """Class displaying the views when a user add a player"""

    def prompt_for_add_last_name(self):
        valid_last_name = False
        while not valid_last_name:
            last_name = input("Entrez le nom de famille: ")
            if last_name != "":
                valid_last_name = True
            else:
                print("Vous devez entrer un nom")
        return last_name
        
    def prompt_for_add_first_name(self):
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Entrez le prénom: ")
            if first_name != "":
                valid_first_name = True
            else:
                print("Vous devez entrer un prénom")
        return first_name
    
    def prompt_for_add_birth_details(self):
        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance: ") # erreur si il n'y a pas de "self"
            if self.birth_day.isdigit() == True and len(self.birth_day) == 2 and int(self.birth_day) < 32:
                valid_day = True
            else: 
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                        
        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance: (En chiffre) ")
            if self.birth_month.isdigit() == True and len(self.birth_month) == 2 and int(self.birth_month) < 13:
                valid_month = True
            else:
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        valid_year = False
        while not valid_year:       
            self.birth_year = input("Entrez l'année de naissance: ")
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4 and int(self.birth_year) < 2021:
                valid_year = True
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980")
        
        return Player.birthdate_list.append(self.birth_day), Player.birthdate_list.append(self.birth_month), Player.birthdate_list.append(self.birth_year)

    def prompt_for_gender(self):
        valid_gender = False
        while not valid_gender:
            gender = input("Choisissez le genre du joueur \n'H' pour un homme \n'F' pour une femme: ")
            if gender == "H":
                valid_gender = True
                return "Homme"
            elif gender == "F":
                valid_gender = True
                return "Femme"
            else:
                print("Vous devez entrer un genre (H ou F)")
 
    def prompt_for_ranking(self):
        valid_ranking = False
        while not valid_ranking:
            ranking = input("Entrez le classement du joueur: ")
            if ranking.isdigit() == True and int(ranking) >= 0:
                valid_ranking = True
            else :
                print("Vous devez entrer un nombre entier positif")
        return ranking


class Player:
    """Contain all the data of a chess player"""
    def __init__(self, last_name="", first_name="", birthdate="", gender="", ranking=""):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        
    birthdate_list = []

    def create_birthdate(self):
        return f"{self.birthdate_list[0]}/{self.birthdate_list[1]}/{self.birthdate_list[2]}"

    
class ControllerAddPlayer:
    """Controllers when a user wants to add a player in the database"""
    
    player_keys = ["Nom", "Prénom", "Date de naissance", "Sexe", "Ranking"]
    player_values = []
    serialized_player = {"Nom" : "", "Prénom" : "", "Date de naissance" : "", "Sexe" : "", "Ranking" : 0}

    def __init__(self, view=None, player=None):
        self.player = player
        self.view = view
    
    def serialise_player(self):
        indice_values = 0
        for keys in ControllerAddPlayer.player_keys:
            ControllerAddPlayer.serialized_player[keys] = ControllerAddPlayer.player_values[indice_values]
            indice_values += 1
    
    def insert_player_in_database(self, player):
        self.player = player
        player_database.insert(self.player)
        
    def run(self):
        # while True:
        last_name = self.view.prompt_for_add_last_name()
        self.player_values.append(last_name)

        first_name = self.view.prompt_for_add_first_name()
        self.player_values.append(first_name)

        birthdate = self.view.prompt_for_add_birth_details()
        birthdate = player.create_birthdate()
        self.player_values.append(birthdate)

        gender = self.view.prompt_for_gender()
        self.player_values.append(gender)

        ranking = self.view.prompt_for_ranking()
        self.player_values.append(ranking)
        
        self.serialise_player()
        self.insert_player_in_database(self.serialized_player)
        print(self.serialized_player)

def main():
    controller = ControllerAddPlayer(view, player)
    controller.run()

view = ViewAddPlayer()
player = Player() 
main()