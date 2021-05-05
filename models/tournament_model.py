import time
import datetime
from operator import itemgetter

from tinydb import TinyDB, Query
tournament_database = TinyDB('models/tournament.json')

from views import view_main
from controllers import main_control
from models import player_model
from controllers import tournament_controller


class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                       location=None,
                       tournament_date=None,
                       number_of_rounds=4, 
                       time_control=None, 
                       description=None,
                       players_ids=None,
                       list_of_tours=None
                       ):

        self.tournament_name = tournament_name
        self.location = location        
        self.tournament_date = tournament_date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_tours = []

        self.players_in_tournament = []
        self.player_database = player_model.player_database
        self.home_menu_controller = main_control.HomeMenuController
        self.player_model = player_model.Player()

    def __str__(self):
        print(f"{self.tournament_name} - {self.list_of_tours}")
        
    def serialized(self):
        tournament_infos = {}
        tournament_infos['Nom du tournoi'] = self.tournament_name
        tournament_infos['Lieu'] = self.location
        tournament_infos['Date'] = self.tournament_date
        tournament_infos['Nombre de match'] = self.number_of_rounds
        tournament_infos['Contrôle du temps'] = self.time_control
        tournament_infos['Description'] = self.description
        tournament_infos["Joueurs"] = self.players_ids
        return tournament_infos

    def unserialized(self, serialized_tournament):
        tournament_name = serialized_tournament['Nom du tournoi']
        location = serialized_tournament['Lieu']
        tournament_date = serialized_tournament['Date']
        number_of_rounds = serialized_tournament['Nombre de match']
        time_control = serialized_tournament['Contrôle du temps']
        description = serialized_tournament['Description']
        players_ids = serialized_tournament["Joueurs"]
        return Tournament(tournament_name, 
                          location,
                          tournament_date,
                          number_of_rounds, 
                          time_control,
                          description,
                          players_ids
                          )

    def add_to_database(self, tournament_values):
        tournament = Tournament(tournament_values[0],
                                tournament_values[1],
                                tournament_values[2],
                                tournament_values[3],
                                tournament_values[4],
                                tournament_values[5],
                                tournament_values[6]
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
        self.player_class = player_model.Player()
        self.round = Round()
        self.list_of_rounds = []
        self.sorted_players = []
        self.list_of_finished_rounds = []
        self.view = view_main.TourDisplay()
        
    def __call__(self):

        self.name = "Tour n°" + str(Tour.TOUR_NUMBER)
        Tour.TOUR_NUMBER += 1

        input("Appuyez sur une touche pour commencer le tour")
        print()
        self.begin_time = datetime.datetime.now()
        input("Appuyez sur une touche lorsque le tour est terminé")
        print()
        self.end_time = datetime.datetime.now()

        # tant qu'il y a des joueurs dans la liste, ajoute des instances de 'Round' dans la liste 'list_of_rounds'
        while len(self.sorted_players) > 0:
            self.list_of_rounds.append(self.round.create_instance(self.sorted_players))
            del self.sorted_players[0]
            del self.sorted_players[0]
        
        self.view.display_tour(self.name, self.list_of_rounds)

        for round in self.list_of_rounds:
            score_player_1 = input(f"Entrez le score de {round.player_1} :")
            round.score_joueur_1 += float(score_player_1)
            score_player_2 = input(f"Entrez le score de {round.player_2} :")
            round.score_joueur_2 += float(score_player_2)
            self.list_of_finished_rounds.append(([round.player_1, round.score_joueur_1], [round.player_2, round.score_joueur_2]))

        print(self.list_of_finished_rounds)
        # self.view.display_score(Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds))
        
        return Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds)

    def __str__(self):
        print(f"{self.name}. Début : {self.begin_time} - Fin : {self.end_time}"
              f"{self.list_of_finished_rounds}"
             )
          
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
    """

    ROUND_NUMBER = 1

    def __init__(self, name=None, player_1=None, player_2=None, score_joueur_1=0, score_joueur_2=0):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_joueur_1 = score_joueur_1
        self.score_joueur_2 = score_joueur_2

    def create_instance(self, list_of_player):
        player_1 = list_of_player[0]
        player_2 = list_of_player[1]    
        name = "Round" + str(Round.ROUND_NUMBER)
        Round.ROUND_NUMBER += 1
        return Round(name, player_1, player_2)
    
    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}."


