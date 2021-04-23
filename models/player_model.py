class Player:
    """Contain all the data of a chess player"""
    def __init__(self, last_name="", first_name="", birthdate="", gender="", ranking=""):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    player_values = []    
    birthdate_list = []