from tinydb import TinyDB, Query
tournament_database = TinyDB('models/tournament.json')

class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_attributes):
        self.tournament_attributes = tournament_attributes