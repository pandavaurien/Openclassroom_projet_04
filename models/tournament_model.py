import time

from tinydb import TinyDB

from views import view_main
from controllers import main_control
from models import player_model

tournament_database = TinyDB('models/tournament.json')


class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                       location=None,
                       tournament_date=None,
                       number_of_rounds=4, 
                       time_control=None, 
                       description=None,
                       players_ids=None,
                       list_of_players=None,
                       list_of_tours=[]
                       ):

        self.tournament_name = tournament_name
        self.location = location        
        self.tournament_date = tournament_date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_players = list_of_players
        self.list_of_tours = list_of_tours
        
        self.player_database = player_model.player_database
        self.home_menu_controller = main_control.HomeMenuController
        self.player_model = player_model.Player()

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n\n {self.list_of_tours}\n"
        
    def serialized(self):
        tournament_infos = {}
        tournament_infos['Nom du tournoi'] = self.tournament_name
        tournament_infos['Lieu'] = self.location
        tournament_infos['Date'] = self.tournament_date
        tournament_infos['Nombre de match'] = self.number_of_rounds
        tournament_infos['Contrôle du temps'] = self.time_control
        tournament_infos['Description'] = self.description
        tournament_infos["Joueurs_id"] = self.players_ids
        tournament_infos["Liste de joueurs"] = self.list_of_players
        tournament_infos["Tours"] = self.list_of_tours
        
        return tournament_infos

    def unserialized(self, serialized_tournament):
        tournament_name = serialized_tournament['Nom du tournoi']
        location = serialized_tournament['Lieu']
        tournament_date = serialized_tournament['Date']
        number_of_rounds = serialized_tournament['Nombre de match']
        time_control = serialized_tournament['Contrôle du temps']
        description = serialized_tournament['Description']
        players_ids = serialized_tournament["Joueurs_id"]
        list_of_players = serialized_tournament["Liste de joueurs"]
        list_of_tours =serialized_tournament["Tours"]
        
        return Tournament(tournament_name, 
                          location,
                          tournament_date,
                          number_of_rounds, 
                          time_control,
                          description,
                          players_ids,
                          list_of_players,
                          list_of_tours                          
                          )

    def add_to_database(self, tournament_values):
        tournament = Tournament(tournament_values[0],
                                tournament_values[1],
                                tournament_values[2],
                                tournament_values[3],
                                tournament_values[4],
                                tournament_values[5],
                                tournament_values[6],
                                tournament_values[7]
                                )
        tournament_database.insert(tournament.serialized())        


class Tour:
    """
    Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs 
    avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé, 
    le gestionnaire du tournoi saisit les résultats de chaque match avant de 
    générer les paires suivantes.
    Les instances de tour doivent être stockées dans une liste sur l'instance
    de tournoi à laquelle elles appartiennent.
    ---
    Renvoi l'instance de tour
    """
    
    TOUR_NUMBER = 1
    
    def __init__(self, name=None, begin_time=None, end_time=None, list_of_finished_rounds=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.player = player_model.Player()
        self.round = Round()
        self.list_of_rounds = []
        self.list_of_finished_rounds = list_of_finished_rounds
        self.view = view_main.TourDisplay()
    
    def __repr__(self):
        return f"{self.name} - Début : {self.begin_time}. Fin : {self.end_time}.\n\n{self.list_of_finished_rounds}\n\n"
        
    def __call__(self, sorted_players_list):
        self.list_of_rounds = []
        self.list_of_finished_rounds = []
        self.name = "Tour n°" + str(Tour.TOUR_NUMBER)
        Tour.TOUR_NUMBER += 1
        
        self.begin_time, self.end_time = self.view.display_tournament_time()

        # tant qu'il y a des joueurs dans la liste, ajoute des instances de 'Round' dans la liste 'list_of_rounds'
        while len(sorted_players_list) > 0:
            self.list_of_rounds.append(self.round.create_instance(sorted_players_list))
            del sorted_players_list[0]
            del sorted_players_list[0]
        
        self.view.display_tour(self.name, self.list_of_rounds)

        for round in self.list_of_rounds:

            valid_score_player_1 = False
            while not valid_score_player_1:
                try:
                    score_player_1 = input(f"Entrez le score de {round.player_1} :")  
                    float(score_player_1)
                except Exception:
                    print("Vous devez entrer 0, 0.5, ou 1")
                else:
                    round.player_1.score_player_1 = float(score_player_1)
                    valid_score_player_1 = True

            valid_score_player_2 = False
            while not valid_score_player_2:
                try:
                    score_player_2 = input(f"Entrez le score de {round.player_2} :")  
                    float(score_player_2)
                except Exception:
                    print("Vous devez entrer 0, 0.5, ou 1")
                else:
                    round.player_2.score_player_2 = float(score_player_2)
                    valid_score_player_2 = True

            self.list_of_finished_rounds.append(([round.player_1, round.player_1.score_player_1], [round.player_2, round.player_2.score_player_2]))
        print()
        return Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds)
          
    
class Round:
    """
    Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
    chacune contenant deux éléments : une référence à une instance de joueur et un score.
    Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
    """

    ROUND_NUMBER = 1

    def __init__(self, name=None, player_1=None, player_2=None, score_player_1=None, score_player_2=None):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2
        
    def create_instance(self, list_of_player):
        player_1 = list_of_player[0]
        player_2 = list_of_player[1]
        score_player_1 = 0
        score_player_2 = 0  
        name = "Round" + str(Round.ROUND_NUMBER)
        Round.ROUND_NUMBER += 1
        return Round(name, player_1, player_2, score_player_1, score_player_2)
    
    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}."



