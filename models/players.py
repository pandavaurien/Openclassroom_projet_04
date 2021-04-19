# coding: utf-8

"""docstring"""
from tinydb import TinyDB, Query
player_database = TinyDB('players.json')


class Player:
    """Contain all the data of a chess player"""
    def __init__(self, last_name="", first_name="", birthdate="", gender="", ranking=""):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        
    birthdate_list = []

    def create_birthdate(self):
        return f"{self.birthdate_list[0]}/{self.birthdate_list[1]}/{self.birthdate_list[2]}"