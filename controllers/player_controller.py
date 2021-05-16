from operator import attrgetter
import pandas as pd

from controllers import main_control
import controllers
from models import player_model
from views import view_main
from controllers import create_menus


class CreatePlayerController:
    """Enter all the player's details, then add the player in the database""" 
    def __init__(self):
        self.player_values = []
        self.player_keys = ["Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]

    def __call__(self): 
        self.player_model = player_model.Player()
        self.player_values.append(self.add_last_name())
        self.player_values.append(self.add_first_name())
        self.player_values.append(self.add_birth_details())
        self.player_values.append(self.add_gender())
        self.player_values.append(self.add_ranking())
        if self.validate_player():
            self.player_model.add_to_database(self.player_values)
        self.player_values.clear()
        main_control.HomeMenuController()
        
    
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
        return int(ranking)

    def validate_player(self):
        view_main.FrameDisplay.display_datas_in_a_frame(self.player_values, self.player_keys)

        validated_choice = False
        while not validated_choice:
            print("Valider ce joueur ? \n"
            "'Y' pour valider, 'N' pour recommencer")
            choice = input("-->")
            if choice == "Y":
                validated_choice = True
            elif choice == "N":
                main_control.HomeMenuController()
            else:
                print("Vous devez entrer 'Y' ou 'N'") 
        return validated_choice 


class PlayerReport:
    """Display the players reports"""

    def __init__(self):
        pass

    def __call__(self):
        self.create_menu = create_menus.CreateMenus()
        self.home_menu_controller = main_control.HomeMenuController()
        self.display_player = view_main.DisplayPlayersReport()
        self.players_database = player_model.player_database
        self.player = player_model.Player()
        player_serialized = []
        
        for player in self.players_database:
            player_serialized.append(self.player.unserialized(player))

        self.display_player()
        entry = self.create_menu(self.create_menu.players_report_menu)
        
        if entry =="1":
            player_serialized.sort(key=attrgetter("last_name"))
            self.display_player.display_alphabetical(player_serialized)
            PlayerReport.__call__(self)
        if entry =="2":
            player_serialized.sort(key=attrgetter("ranking"))
            self.display_player.display_ranking(player_serialized)
            PlayerReport.__call__(self)
        if entry == "3":
            self.home_menu_controller()


       

        

    

