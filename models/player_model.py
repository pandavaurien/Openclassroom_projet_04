import time

from tinydb import TinyDB, Query
import pandas as pd

from controllers import main_control
pd.set_option('display.max_rows', None)
player_database = TinyDB('models/players.json')


class Player:
    def __init__(self, last_name=None, first_name=None, birthdate=None, gender=None, ranking=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.home_menu_controller = main_control.HomeMenuController()
        self.function = main_control.Function()

    def __repr__(self):
        return f"Nom :{self.last_name} Prénom : {self.first_name} classement :{self.ranking}"    

    def __str__(self):
        return f"""Nom :{self.last_name} Prénom : {self.first_name} classement :{self.ranking}"""

            
    
    

    