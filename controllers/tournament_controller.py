import time
import copy
from operator import itemgetter
from operator import attrgetter

import pandas as pd
from tinydb import TinyDB, Query

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
        
        # itère dans les ids de joueurs, puis classe les ids des joueurs par ordre de classement
        for id in self.players_ids:
            player = player_model.player_database.get(doc_id=id) 
            self.players_serialized.append(player)
        self.players_serialized.sort(key=itemgetter("Classement"), reverse=True)
        self.players_ids.clear()

        for player in self.players_serialized:
            self.players_ids.append(player.doc_id)
        self.tournament_values.append(self.players_ids.copy())

        
class StartTournament:
    """Docstring"""

    MATCHS_PLAYED = []

    def __init__(self):
        pass
                                    
    def __call__(self):
        self.sorted_players = []
        self.tournament_menu_controller = main_control.TournamentMenuController()
        self.tour = tournament_model.Tour()
        self.view_final_scores = view_main.EndTournamentDisplay()
        
        self.tournament_object = self.select_a_tournament() # Ask to choose a tournament and return an instance of tournament
        if self.tournament_object.list_of_tours != []:
            print("\nLe tournoi à déja eu lieu, veuillez en choisir un autre\n")
            time.sleep(1)
            self.tournament_menu_controller()
        self.sorted_players = self.sort_player_first_tour(self.tournament_object) # copy in the list "sorted_players" the players by ranking
        self.tournament_object.list_of_tours.append(self.tour.run(self.sorted_players)) # 1st tour, copy the instance in tournament
        
        # all the others tours
        for tour in range(int(self.tournament_object.number_of_tours) - 1):
            self.sorted_players.clear()
            self.sorted_players = self.sort_players_by_score(self.tournament_object.list_of_tours[tour])
            self.tournament_object.list_of_tours.append(self.tour.run(self.sorted_players))
        
        self.add_tournament_to_db(self.tournament_object)

    def add_tournament_to_db(self, tournament_object):
        Name = Query()
        tour_to_db = []
        tour_ids = []
        db_tournament = tournament_model.tournament_database
        db_players = player_model.player_database
        tournament_id = db_tournament.get(Name["Nom du tournoi"] == self.tournament_object.tournament_name).doc_id
        # tournament_table = db_tournament.table("_default")
        tours_table = db_tournament.table("tours")

        tournament_serialized = self.tournament_object.serialized()
        
        for tour in tournament_serialized['Tours']:
            tour_serialized = tour.serialized()         
            tour_to_db.clear()
            for match in tour_serialized['Matchs']:
                player_1_and_result = []
                player_2_and_result = []
                player_1_id = db_players.get(Name["Nom"] == match[0][0].last_name).doc_id
                player_1_and_result = [player_1_id, match[0][1]]
                print(player_1_and_result)
                player_2_id = db_players.get(Name["Nom"] == match[1][0].last_name).doc_id
                player_2_and_result = [player_2_id, match[1][1]]
                print(player_2_and_result)               
                tour_to_db.append([player_1_and_result, player_2_and_result])
            tour_id = tours_table.insert({"Matchs" :tour_to_db})
            tour_ids.append(tour_id)    
               
                
            db_tournament.update({"Tours" : tour_ids}, doc_ids=[tournament_id])

        print(tour_to_db)
        input()           
        # db_tournament.update({"Tours" : tour_to_db}, doc_ids=[tournament_table.doc_id])
                
        self.view_final_scores(self.tournament_object)
               
    def select_a_tournament(self):
        self.tournament = tournament_model.Tournament()

        display_tournament = pd.read_json("models/tournament.json")
        print(display_tournament) #TODO Afficher dans le view

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
        self.player = player_model.Player()
        sorted_players = []
        players_instances = []
      
        for id in tournament.players_ids:
            player =  player_model.player_database.get(doc_id=id)
            player = self.player.unserialized(player)
            players_instances.append(player)
        
        for player in players_instances:
            player_1 = player
            index_player_1 = players_instances.index(player)
            
            """ I divide the number of players by 2, and I add the result to the index
            example : For 8 players, I add 4 to the first index,
            player[0] against player [4],
            player[1] against player [5] etc..."""
            if index_player_1 + len(tournament.players_ids) / 2 < len(tournament.players_ids):
                index_player_2 = index_player_1 + int(len(tournament.players_ids) / 2)
                player_2 = players_instances[index_player_2]
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                self.MATCHS_PLAYED.append({player_1, player_2})
            else:
                pass
        
        return sorted_players

    def sort_players_by_score(self, tour_instance):
        """ return a list of players sorted by score"""
        players = []
        players_sorted_by_score = []
        players_sorted_flat = []
        match_to_try = set()
    
        for match in tour_instance.list_of_finished_matchs:
            for player in match:
                players.append(player)
        
        players_sorted_by_score = copy.copy(players)
        
        for player in players_sorted_by_score:
            players_sorted_flat.append(player[0])

        players_sorted_by_score.clear()
     
        #Sort players by score, if score are equals, sort by rank.
        players_sorted_flat.sort(key=attrgetter("tournament_score", 'ranking'), reverse=True)

        for player_1 in players_sorted_flat:

            if player_1 in players_sorted_by_score:
                continue
            else:
                try:
                    player_2 = players_sorted_flat[players_sorted_flat.index(player_1) + 1]
                except:
                    break
                            
            match_to_try.add(player_1) 
            match_to_try.add(player_2) 

            while match_to_try in self.MATCHS_PLAYED: # compare match_to_try avec les match déjà joués    
                print(f"Le match {match_to_try} a déjà eu lieu")
                time.sleep(1)
                match_to_try.remove(player_2)                
                try:
                    player_2 = players_sorted_flat[players_sorted_flat.index(player_2) + 1]
                except:
                    break
                match_to_try.add(player_2)
                continue
                    
            else:
                print(f"Ajout du match {match_to_try}")
                players_sorted_by_score.append(player_1)
                players_sorted_by_score.append(player_2)
                players_sorted_flat.pop(players_sorted_flat.index(player_2))
                self.MATCHS_PLAYED.append({player_1, player_2})
                match_to_try.clear()              
                time.sleep(1)

        return players_sorted_by_score


class TournamentReport:
    """Display the tournament reports"""

    def __call__(self):
        self.clear = view_main.ClearScreen()
        self.create_menu = create_menus.CreateMenus()
        self.display_tournament = view_main.DisplayTournamentsReport()
        self.display_player = view_main.DisplayPlayersReport()
        self.home_menu_controller = main_control.HomeMenuController()
        
        self.players_database = player_model.player_database
        self.player = player_model.Player()
        player_serialized = []
        self.tournament_database = tournament_model.tournament_database
        self.tournament = tournament_model.Tournament()
        tournament_serialized = []
        tournament_objects = []

        for tournament in self.tournament_database:
            tournament_objects.append(tournament)
            tournament_serialized.append(self.tournament.unserialized(tournament))

        self.clear()                 
        self.display_tournament()
        entry = self.create_menu(self.create_menu.tournaments_report_menu)

        if entry == "1":
            for tournament in tournament_serialized:
                for id in tournament.players_ids:
                    player = self.players_database.get(doc_id=id)
                    player_serialized.append(self.player.unserialized(player))
            self.display_tournament.display_tournaments(tournament_serialized, player_serialized)
            player_serialized.clear()
            self.home_menu_controller()
            
        if entry == "2":
            self.display_tournament.choose_a_tournament()
            while True:
                print("Entrez le numéro correspondant")
                choice_id = input("-->")

                for tournament in tournament_objects:
                    if int(choice_id) == tournament.doc_id:
                        tournament_object = self.tournament_database.get(doc_id=int(choice_id))
                        tournament_object = self.tournament.unserialized(tournament_object)
                        if tournament_object.list_of_tours == []:
                            print("\nLe tournoi n'a pas encore eu lieu, vous ne pouvez pas afficher les résultats\n")
                            time.sleep(1)
                        
                        else:
                            entry = self.create_menu(self.create_menu.tournaments_report_menu_2)
                            if entry == "1":
                                entry = self.create_menu(self.create_menu.players_report_menu)
                                if entry == "1":
                                    for id in tournament_object.players_ids:
                                        player = self.players_database.get(doc_id=int(id))
                                        player_serialized.append(self.player.unserialized(player))
                                    player_serialized.sort(key=attrgetter("last_name"))
                                    self.display_player.display_alphabetical(player_serialized)
                                    player_serialized.clear()
                                    TournamentReport.__call__(self)
                                if entry == "2":
                                    for id in tournament_object.players_ids:
                                        player = self.players_database.get(doc_id=int(id))
                                        player_serialized.append(self.player.unserialized(player))
                                    player_serialized.sort(key=attrgetter("ranking"))
                                    self.display_player.display_ranking(player_serialized)
                                    player_serialized.clear()
                                    TournamentReport.__call__(self)
                            if entry == "2":
                                for tour in tournament_object.list_of_tours:
                                    print(tour)
                            if entry == "3":
                                pass # afficher les matchs
                            if entry == "4":
                                self.home_menu_controller()

                print("Vous devez entrer le numéro correspondant au tournoi")
    
        if entry == "3":
            self.home_menu_controller()






    






    
        






        




