import time
import datetime
from operator import itemgetter
from operator import attrgetter

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

    # def __str__(self):
    #     print(f"{self.tournament_name} - {self.list_of_tours}")
        
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
    MATCHS_PLAYED = []

    def __init__(self, name=None, begin_time=None, end_time=None, list_of_finished_rounds=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.player = player_model.Player()
        self.round = Round()
        self.list_of_rounds = []
        # self.sorted_players = []
        self.list_of_finished_rounds = []
        self.view = view_main.TourDisplay()
        
    def __call__(self, sorted_players_list):

        self.name = "Tour n°" + str(Tour.TOUR_NUMBER)
        Tour.TOUR_NUMBER += 1

        input("Appuyez sur une touche pour commencer le tour")
        print()
        self.begin_time = datetime.datetime.now()
        print(f"Début du tour : {self.begin_time}")
        print()
        input("Appuyez sur une touche lorsque le tour est terminé")
        print()
        self.end_time = datetime.datetime.now()
        print(f"Fin du tour : {self.end_time}")
        print()

        # tant qu'il y a des joueurs dans la liste, ajoute des instances de 'Round' dans la liste 'list_of_rounds'
        while len(sorted_players_list) > 0:
            self.list_of_rounds.append(self.round.create_instance(sorted_players_list))
            del sorted_players_list[0]
            del sorted_players_list[0]
        
        self.view.display_tour(self.name, self.list_of_rounds)

        for round in self.list_of_rounds:
            score_player_1 = input(f"Entrez le score de {round.player_1} :") #TODO faire une fonction pour vérifier l'input
            round.player_1.tournament_score += float(score_player_1)
            score_player_2 = input(f"Entrez le score de {round.player_2} :")
            round.player_2.tournament_score += float(score_player_2)
            self.list_of_finished_rounds.append(([round.player_1, round.player_1.tournament_score], [round.player_2, round.player_2.tournament_score]))
        print()
        print("Score :" + str(self.list_of_finished_rounds))
        print()
        print("Matchs déja joués : " + str(Tour.MATCHS_PLAYED))
        print()

        # self.view.display_score(Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds))
        
        return Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds)
          
    def sort_player_first_tour(self, tournament):
        """ return a list of players sorted by ranking"""
        sorted_players = []
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
            player_1 = self.player.unserialized(player)
            index_player_1 = players_serialized.index(player)

            """ Je divise le nombre de joueurs par 2, et j'ajoute le résultat à l'indice
            exemple : Pour 8 joueurs, j'ajoute 4 au premier indice,
            joueur[0] contre joueur [4],
            joueur[1] contre joueur [5] etc..."""
            if index_player_1 + len(players_serialized) / 2 < len(players_serialized):
                player_2 = self.player.unserialized(players_serialized[index_player_1 + int(len(players_serialized) / 2)])
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                Tour.MATCHS_PLAYED.append({player_1, player_2})
            else:
                pass
        return sorted_players

    def sort_players_by_score(self):
        """ return a list of players sorted by score"""
        players_sorted_by_score = []
        players_sorted_flat = []
        round_to_try = set()
                        
        for round in self.list_of_finished_rounds:
            for player in round:
                players_sorted_by_score.append(player)
        print(players_sorted_by_score)

        for player in players_sorted_by_score:
            player.pop()
            players_sorted_flat.append(player[0])

        players_sorted_flat.sort(key=attrgetter("tournament_score", 'ranking'), reverse=True)
        print()
        print(players_sorted_flat)

        
                
        
            
        # print(players_sorted_flat)
        # players_sorted_by_score.clear()

        # for player_1 in players_sorted_flat:
            
        #     player_2 = players_sorted_flat[players_sorted_flat.index(player_1) + 1]

        #     if player_1 in players_sorted_by_score:
        #         continue
            
        #     round_to_try.add(player_1) 
        #     round_to_try.add(player_2) 

        #     if round_to_try in Tour.MATCHS_PLAYED: # compare round_to_try avec les match déjà joués
        #         print(f"Le match {round_to_try} a déjà eu lieu")
        #         player_2 = players_sorted_flat[players_sorted_flat.index(player_1) + 1]
        #         time.sleep(1)

        #         # round_to_try.remove(player_2)
        #         # player_to_try_index += 1
        #     else:
        #         print(f"Ajout du match {round_to_try}")
        #         players_sorted_by_score.append(player_1)
        #         players_sorted_by_score.append(player_2)
                
        #         round_to_try.clear()              
        #         time.sleep(1)

        return players_sorted_by_score


class Round:
    """
    Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
    chacune contenant deux éléments : une référence à une instance de joueur et un score.
    Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
    """

    ROUND_NUMBER = 1

    def __init__(self, name=None, player_1=None, player_2=None):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        # self.score_joueur_1 = score_joueur_1
        # self.score_joueur_2 = score_joueur_2

    def create_instance(self, list_of_player):
        player_1 = list_of_player[0]
        player_2 = list_of_player[1]    
        name = "Round" + str(Round.ROUND_NUMBER)
        Round.ROUND_NUMBER += 1
        return Round(name, player_1, player_2)
    
    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}."



