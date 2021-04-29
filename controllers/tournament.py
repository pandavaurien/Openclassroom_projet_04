import time

import pandas as pd

from controllers import main_control
from controllers import create_menus
from models import tournament_model
from models import player_model
from views import view_main
from controllers import functions

class CreateTournamentController:
    """docstring"""
    
    def __init__(self):
        self.create_menu = create_menus.CreateMenus()
        self.tournament_values = []
        self.tournament_keys = ["Nom", "Lieu", "Date", "Nombre de tours", "Contrôle du temps", "Description", "Joueurs"]
        # self.tournament_dict = {}
        self.players_in_tournament = []
        self.player = player_model.Player()
        self.home_menu_controller = main_control.HomeMenuController()

    def __call__(self):
        self.tournament_values.append(self.add_tournament_name())
        self.tournament_values.append(self.add_location())
        self.tournament_values.append(self.add_tournament_date())
        self.tournament_values.append(self.add_number_of_rounds())
        self.tournament_values.append(self.add_time_control())
        self.tournament_values.append(self.add_description())
        print(self.tournament_values)
        self.add_players_to_tournament()

    def add_tournament_name(self):
        valid_tournament_name = False
        while not valid_tournament_name:
            tournament_name = input("Entrez le nom du tournoi: ")
            if tournament_name != "":
                valid_tournament_name = True
            else:
                print("Vous devez entrer un nom")
        return tournament_name

    def add_location(self):
        valid_location = False
        while not valid_location:
            location = input("Entrez l'endroit où se déroule le tournoi: ")
            if location != "":
                valid_location = True
            else:
                print("Vous devez entrer un endroit")
        return location

    def add_tournament_date(self):
        date_list = []

        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour du tournoi: ")
            if self.birth_day.isdigit() == True and len(self.birth_day) == 2 and int(self.birth_day) < 32:
                valid_day = True
                date_list.append(self.birth_day)
            else: 
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                        
        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois du tournoi: (En chiffre) ")
            if self.birth_month.isdigit() == True and len(self.birth_month) == 2 and int(self.birth_month) < 13:
                valid_month = True
                date_list.append(self.birth_month)
            else:
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        valid_year = False
        while not valid_year:       
            self.birth_year = input("Entrez l'année du tournoi: ")
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4 and int(self.birth_year) < 2021:
                valid_year = True
                date_list.append(self.birth_year)
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980)")

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def add_number_of_rounds(self):
        number_of_rounds = 4
        print("Le nombre de rounds est de 4 par défaut\n"
        "Souhaitez-vous changer ce nombre ?\n"
        "Entrer 'Y' pour changer, ou 'N' pour continuer")
        valid_number = False
        while not valid_number:
            choice = input("--> ")
            if choice == "Y":
                number_of_rounds = input("Entrez le nombre de rounds :")
                if number_of_rounds.isdigit() :
                    valid_number = True
                else:
                    print("Vous devez entrer un nombre entier")
                    self.add_number_of_rounds()              
            if choice == "N":
                valid_number = True
        return number_of_rounds

    def add_time_control(self):
        print("Choisissez le contrôle du temps:")
        time_control = None
        entry = self.create_menu(self.create_menu.time_control_menu)
        if entry == "1":
            time_control = "Bullet"
        if entry == "2":
            time_control = "Blitz"
        if entry == "3":
            time_control = "Coup rapide"
        return time_control
    
    def add_description(self):
        description = input("Entrer une description au tournoi :\n"
        "-->")
        return description

    def add_players_to_tournament(self):
        view_main.ClearScreen()

        valid_add_player_choice = False
        while not valid_add_player_choice:
            add_player_choice = input("Voulez-vous ajouter un joueur ?\n"
            "Appuyer sur 'Y' pour confirmer, ou 'N' pour quitter")
            if add_player_choice == "Y":
                valid_add_player_choice = True
            elif add_player_choice == "N":
                self.home_menu_controller()
            else:
                print("Appuyez sur 'Y' ou 'N'")

        if len(self.players_in_tournament) >= 8: 
            print()
            print("Vous avez déjà 8 joueurs dans le tournoi")
            time.sleep(2)
            self.home_menu_controller()

        display_players_database = pd.read_json("models/players.json")
        print(display_players_database)
        print()
        print("Vous devez choisir 8 joueurs maximum pour un tournoi")
        print()
        print("Joueurs dans le tournoi : " + str(self.players_in_tournament))
        print()
        print("Entrez le numéro du joueur :")
        
        valid_id = False
        while not valid_id:
            id_choice = input("--> ")
            if int(id_choice):
                valid_id = True
            else:
                print("Vous devez entrer un nombre entier")
        
        id_choice = int(id_choice)

        if id_choice <= 0 or id_choice > len(player_model.player_database):
            print()
            print("vous devez choisir un joueur dans la liste")
            print()
            print("Joueurs dans le tournoi : " + str(self.players_in_tournament))
            time.sleep(1)
            
            self.add_players_to_tournament()
     
        if id_choice in self.players_in_tournament:
            print("\nVous avez déjà choisi ce joueur dans ce tournoi\n")
            print("Joueurs dans le tournoi : " + str(self.players_in_tournament))
            print()
            time.sleep(1)
            self.add_players_to_tournament()

        self.players_in_tournament.append(id_choice)
        print("Joueurs dans le tournoi : " + str(self.players_in_tournament))
        self.add_players_to_tournament()

        

        # player_choosen = player_model.player_database.get(doc_id=id_choice)
        # print(f"{player_choosen['Nom']} {player_choosen['Prénom']} {player_choosen['Classement']}")

        # print("Joueurs dans le tournoi : " + str(self.players_in_tournament))
                  
        #       #db.get(doc_id="")
        # player_instance = self.player(player_choosen)
        # print(player_instance)
        



        




