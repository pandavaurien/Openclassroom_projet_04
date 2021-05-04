import time
from operator import itemgetter

import pandas as pd

from controllers import main_control
from controllers import create_menus
from models import tournament_model
from models import player_model
from views import view_main

class CreateTournamentController:
    """docstring"""
    
    def __init__(self):
        self.create_menu = create_menus.CreateMenus()
        self.tournament_values = []
        # self.tournament_keys = ["Nom", "Lieu", "Date", "Nombre de tours", "Contrôle du temps", "Description", "Joueurs"]
        self.players_in_tournament = []
        self.player = player_model.Player()
        self.home_menu_controller = main_control.HomeMenuController()
        self.tournament = tournament_model.Tournament()
        
    def __call__(self):
        self.tournament_values.append(self.add_tournament_name())
        self.tournament_values.append(self.add_location())
        self.tournament_values.append(self.add_tournament_date())
        self.tournament_values.append(self.add_number_of_rounds())
        self.tournament_values.append(self.add_time_control())
        self.tournament_values.append(self.add_description())
        self.add_players_to_tournament()
        self.tournament_values.append(self.players_in_tournament)
        self.tournament.add_to_database(self.tournament_values)
        self.tournament.add_players_of_tournament_in_database(self.players_in_tournament)
        self.home_menu_controller()
       
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
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4:
                valid_year = True
                date_list.append(self.birth_year)
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980)")

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def add_number_of_rounds(self):
        number_of_rounds = 4
        print("Le nombre de rounds est de 4 par défaut\n"
        "Souhaitez-vous changer ce nombre ?")
        
        valid_number = False
        while not valid_number:
            print("Entrer 'Y' pour changer, ou 'N' pour continuer")
            choice = input("--> ")
            if choice == "Y":
                number_of_rounds = input("Entrez le nombre de rounds :")
                if number_of_rounds.isdigit() :
                    valid_number = True
                else:
                    print("Vous devez entrer un nombre entier")            
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
        """Add the ids of the selected players in a list, en return the list"""
        view_main.ClearScreen()
        id_choice = None

        valid_add_player_choice = False
        while not valid_add_player_choice:
            add_player_choice = input("\nVoulez-vous ajouter un joueur ?\n\n"
            "Appuyer sur 'Y' pour confirmer, ou 'N' pour poursuivre")
            if add_player_choice == "Y":
                valid_add_player_choice = True
            elif add_player_choice == "N":
                return
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


class StartTournament:
    """Docstring"""
    def __init__(self):
        
        self.tour = Tour()
        self.tournament = tournament_model.Tournament()
        self.tournament_object = None
        
    def __call__(self):
        self.tournament_object = self.select_a_tournament() # demande de choisir un tournoi et renvoi une instance de Tournament
        self.tour.sort_player_by_rank(self.tournament_object) # copie dans la liste "sorted_players" les joueurs triés par classement
        # for tour in range (self.tournament_object.number_of_rounds): # 
        self.tour()

    def select_a_tournament(self):
        display_tournament = pd.read_json("models/tournament.json")
        print(display_tournament)

        valid_entry = False
        while not valid_entry:
            print("Entrez le chiffre correspondant au tournoi")
            choice = input("--> ")
            try:
                choice.isdigit() == False
                int(choice) > len(tournament_model.tournament_database)
                int(choice) <= 0
            except Exception:
                print("Vous devez entrer le chiffre correspondant au tournoi")
            
            else:
                choosen_tournament = tournament_model.tournament_database.get(doc_id=int(choice))
                tournament_object = self.tournament.unserialized(choosen_tournament)
                # print(tournament_object.__str__())
                return tournament_object
    



class Tour:
    """
    Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs 
    avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé, 
    le gestionnaire du tournoi saisit les résultats de chaque match avant de 
    générer les paires suivantes.
    """
    tour_number = 1

    def __init__(self, name=None, begin_time=None, end_time=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.player_class = player_model.Player()
        self.round = Round()
        self.list_of_rounds = []
        self.sorted_players = []
        
    def __call__(self):
        # tant qu'il y a des joueurs dans la liste, ajoute des instances de 'Round' dans la liste 'list_of_rounds'
        while len(self.sorted_players) > 0:
            self.list_of_rounds.append(self.round.create_instance(self.sorted_players))
            del self.sorted_players[0]
            del self.sorted_players[0]
       
   
    def sort_player_by_rank(self, tournament):
        players_serialized = []
        id_list = tournament.players_ids
        
        # itère dans les ids de joueurs, puis classe les joueurs par ordre de classement
        for id in id_list:
            player = player_model.player_database.get(doc_id=id) 
            players_serialized.append(player)
        players_serialized.sort(key=itemgetter("Classement"), reverse=True)

        # itère dans la liste de joueurs, créé une instance de joueur à chaque itération
        # et copie chaque instance dans la liste 'sorted_player'
        for player in players_serialized:
            player_object = self.player_class.unserialized(player)
            self.sorted_players.append(player_object)

    def sort_players_by_score(self):
        pass

    


class Round:
    """
    Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
    chacune contenant deux éléments : une référence à une instance de joueur et un score.
    Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.

    Les instances de round doivent être stockées dans une liste sur l'instance
    de tournoi à laquelle elles appartiennent.
    """

    round_number = 1

    def __init__(self, name=None, player_1=None, player_2=None, score_joueur_1=0, score_joueur_2=0):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_joueur_1 = score_joueur_1
        self.score_joueur_2 = score_joueur_2

    def create_instance(self, list_of_player):
        player_1 = list_of_player[0]
        player_2 = list_of_player[1]
    
        name = "Round" + str(Round.round_number)
        Round.round_number += 1
        print(Round(name, player_1, player_2))
        return Round(name, player_1, player_2)
    
    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}. Score : {self.score_joueur_1} - {self.score_joueur_2}"

    
        






        




