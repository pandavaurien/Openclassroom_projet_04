import time

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
                       players_ids=None):

        self.tournament_name = tournament_name
        self.location = location        
        self.tournament_date = tournament_date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids

        self.players_in_tournament = []
        self.player_database = player_model.player_database
        self.home_menu_controller = main_control.HomeMenuController
        self.player_model = player_model.Player()
        # self.tournament_controller = tournament_controller.CreateTournamentController()

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

    def add_players_of_tournament_in_database(self, ids_list):
        """Iterate in the list of selected ids, then add the players in the tournament database"""
        player_number = 1
        player_name = f"Joueur {player_number}"

        for player in ids_list:
            player_to_add = player_model.player_database.get(ids_list, doc_id=player)
            print(f"Joueur ajouté au tournoi : {player_to_add['Nom']} {player_to_add['Prénom']}, classement : {player_to_add['Classement']}" )


