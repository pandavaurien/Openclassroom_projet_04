import pandas as pd

from controllers import main_control
from models import player_model
from views import view_main


class CreatePlayerController:
    """Enter all the player's details, then add the player in the database""" 
    def __init__(self):
        self.player_values = []
        self.player_keys = ["Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]
        self.home_menu_controller = main_control.HomeMenuController()

    def __call__(self): 
        self.player_values.append(self.add_last_name())
        self.player_values.append(self.add_first_name())
        self.player_values.append(self.add_birth_details())
        self.player_values.append(self.add_gender())
        self.player_values.append(self.add_ranking())

        view_main.FrameDisplay.display_datas_in_a_frame(self.player_values, self.player_keys)

        # Crée un objet player
        self.player_object = player_model.Player(self.player_values[0],
                                                 self.player_values[1],
                                                 self.player_values[2],
                                                 self.player_values[3], 
                                                 self.player_values[4]
                                                 )

        # J'ajoute les attributs de l'objet player_object dans la base de données.
        self.add_player_to_database({
                                self.player_keys[0] : self.player_object.last_name,
                                self.player_keys[1] : self.player_object.first_name,
                                self.player_keys[2] : self.player_object.birthdate,
                                self.player_keys[3] : self.player_object.gender,
                                self.player_keys[4] : self.player_object.ranking
                                }) 
        self.home_menu_controller()
    
    def add_last_name(self):
        valid_last_name = False
        while not valid_last_name:
            last_name = input("Entrez le nom de famille: ")
            if last_name != "":
                valid_last_name = True
            else:
                print("Vous devez entrer un nom")
        return last_name
        
    def add_first_name(self):
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Entrez le prénom: ")
            if first_name != "":
                valid_first_name = True
            else:
                print("Vous devez entrer un prénom ")
        return first_name

    def add_birth_details(self):
        birthdate_list = []

        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance: ")
            if self.birth_day.isdigit() == True and len(self.birth_day) == 2 and int(self.birth_day) < 32:
                valid_day = True
                birthdate_list.append(self.birth_day)
            else: 
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                        
        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance: (En chiffre) ")
            if self.birth_month.isdigit() == True and len(self.birth_month) == 2 and int(self.birth_month) < 13:
                valid_month = True
                birthdate_list.append(self.birth_month)
            else:
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        valid_year = False
        while not valid_year:       
            self.birth_year = input("Entrez l'année de naissance: ")
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4 and int(self.birth_year) < 2021:
                valid_year = True
                birthdate_list.append(self.birth_year)
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980)")

        return f"{birthdate_list[0]}/{birthdate_list[1]}/{birthdate_list[2]}"

    def add_gender(self):
        valid_gender = False
        validated_gender = None
        while not valid_gender:
            gender = input("Choisissez le genre du joueur \n"
            "'H' pour un homme \n'F' pour une femme: ")
            if gender == "H":
                valid_gender = True
                validated_gender = "Homme"
            elif gender == "F":
                valid_gender = True
                validated_gender = "Femme"
            else:
                print("Vous devez entrer un genre (H ou F)")
        return validated_gender

    def add_ranking(self):
        valid_ranking = False
        while not valid_ranking:
            ranking = input("Entrez le classement du joueur: ")
            if ranking.isdigit() == True and int(ranking) >= 0:
                valid_ranking = True
            else :
                print("Vous devez entrer un nombre entier positif")
        return ranking

    def add_player_to_database(self, player):
        valid_choice = False
        while not valid_choice:
            print("Valider ce joueur ? \n"
            "'Y' pour valider, 'N' pour recommencer")
            choice = input("-->")
            if choice == "Y":
                valid_choice = True
                player_model.player_database.insert(player)
                self.player_values.clear()
                main_control.HomeMenuController() 
            elif choice == "N":
                valid_choice = True
                main_control.HomeMenuController()
            else:
                print("Vous devez entrer 'Y' ou 'N'")

    

