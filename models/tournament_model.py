from tinydb import TinyDB, Query
tournament_database = TinyDB('models/tournament.json')

class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                       location=None,
                       number_of_rounds=4, 
                       tournament_date=None, 
                       time_control=None, 
                       description=None ):

        self.tournament_name = tournament_name
        self.location = location
        self.number_of_rounds = number_of_rounds
        self.tournament_date = tournament_date
        self.time_control = time_control
        self.description = description