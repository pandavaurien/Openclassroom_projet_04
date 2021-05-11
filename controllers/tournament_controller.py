import time
from operator import itemgetter
from operator import attrgetter

import pandas as pd
from tinydb import Query

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
        self.players_in_tournament = []
        self.players_ids = []
        self.players_serialized = []
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
        # self.tournament.add_players_of_tournament_in_database(self.players_in_tournament)
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

        if len(self.players_ids) >= 8: 
            print()
            print("Vous avez déjà 8 joueurs dans le tournoi")
            time.sleep(2)
            self.add_players_to_tournament()

        display_players_database = pd.read_json("models/players.json")
        print(display_players_database)
        print()
        print("Vous devez choisir 8 joueurs maximum pour un tournoi")
        print()
        print("Joueurs dans le tournoi : " + str(self.players_ids))
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
            print("Joueurs dans le tournoi : " + str(self.players_ids))
            time.sleep(1)
            self.add_players_to_tournament()
     
        if id_choice in self.players_ids:
            print("\nVous avez déjà choisi ce joueur dans ce tournoi\n")
            print("Joueurs dans le tournoi : " + str(self.players_ids))
            print()
            time.sleep(1)
            self.add_players_to_tournament()

        # if len(self.players_ids) % 2 != 0:
        #     print("Vous devez avoir un nombre de joueurs pair")
        #     print()
        #     time.sleep(1)
        #     self.add_players_to_tournament()

        self.players_ids.append(id_choice)
        print("Joueurs dans le tournoi : " + str(self.players_ids))
        self.add_players_to_tournament()
        
        # itère dans les ids de joueurs, puis classe les joueurs par ordre de classement
        # et copie les joueurs sérialisés dans la base de données du tournoi.
        for id in self.players_ids:
            player = player_model.player_database.get(doc_id=id) 
            self.players_serialized.append(player)
        self.players_serialized.sort(key=itemgetter("Classement"), reverse=True)
        self.tournament_values.append(self.players_ids.copy())
        self.tournament_values.append(self.players_serialized.copy())
        
        
class StartTournament:
    """Docstring"""

    MATCHS_PLAYED = []

    def __init__(self):
        self.tour = tournament_model.Tour()
        self.tournament = tournament_model.Tournament()
        self.player = player_model.Player()
        self.tournament_object = None
        self.view_tour = view_main.TourDisplay()
        self.view_final_scores = view_main.EndTournamentDisplay()
        self.sorted_players = []
            
    def __call__(self):
        self.tournament_object = self.select_a_tournament() # demande de choisir un tournoi et renvoi une instance de Tournament
        self.sorted_players = self.sort_player_first_tour(self.tournament_object) # copie dans la liste "sorted_players" les joueurs triés par classement
        self.tournament_object.list_of_tours.append(self.tour(self.sorted_players)) # 1er tour, joueurs triés par classement, copie l'instance de tour dans tournament
        
        for tour in range(int(self.tournament_object.number_of_rounds) -1):
            self.sorted_players.clear()
            self.sorted_players = self.sort_players_by_score()
            self.tournament_object.list_of_tours.append(self.tour(self.sorted_players))

        self.view_final_scores(self.tournament_object)
               
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
                return tournament_object

    def sort_player_first_tour(self, tournament):
        """ return a list of players sorted by ranking"""
        sorted_players = []
        players_serialized = []
        
        players_serialized = tournament.list_of_players
                
        # itère dans la liste de joueurs, créé une instance de joueur à chaque itération
        for player in players_serialized:
            player_1 = self.player.unserialized(player)
            # self.tournament.unserialized(tournament)
            index_player_1 = players_serialized.index(player)

            """ I divide the number of players by 2, and I add the result to the index
            example : For 8 players, I add 4 to the first index,
            player[0] against player [4],
            player[1] against player [5] etc..."""
            if index_player_1 + len(players_serialized) / 2 < len(players_serialized):
                player_2 = self.player.unserialized(players_serialized[index_player_1 + int(len(players_serialized) / 2)])
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                self.MATCHS_PLAYED.append({player_1, player_2})
            else:
                pass
            
        return sorted_players

    def sort_players_by_score(self):
        """ return a list of players sorted by score"""
        players_sorted_by_score = []
        players_sorted_flat = []
        round_to_try = set()
    
        for round in self.tour.list_of_finished_rounds:
            for player in round:
                players_sorted_by_score.append(player)
        # print(players_sorted_by_score)

        for player in players_sorted_by_score:
            player.pop()
            players_sorted_flat.append(player[0])

        #Sort players by score, if score are equals, sort by rank.
        players_sorted_flat.sort(key=attrgetter("tournament_score", 'ranking'), reverse=True)
        players_sorted_by_score.clear()

        for player_1 in players_sorted_flat:

            if player_1 in players_sorted_by_score:
                continue
            else:
                try:
                    player_2 = players_sorted_flat[players_sorted_flat.index(player_1) + 1]
                except:
                    break
                            
            round_to_try.add(player_1) 
            round_to_try.add(player_2) 

            while round_to_try in self.MATCHS_PLAYED: # compare round_to_try avec les match déjà joués    
                print(f"Le match {round_to_try} a déjà eu lieu")
                time.sleep(1)
                round_to_try.remove(player_2)                
                try:
                    player_2 = players_sorted_flat[players_sorted_flat.index(player_2) + 1]
                except:
                    break
                round_to_try.add(player_2)
                continue
                    
            else:
                print(f"Ajout du match {round_to_try}")
                players_sorted_by_score.append(player_1)
                players_sorted_by_score.append(player_2)
                players_sorted_flat.pop(players_sorted_flat.index(player_2))
                self.MATCHS_PLAYED.append({player_1, player_2})
                round_to_try.clear()              
                time.sleep(1)

        return players_sorted_by_score

    class TournamentReport:
        pass

    




    
        






        




