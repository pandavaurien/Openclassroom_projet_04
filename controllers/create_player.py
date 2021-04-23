
from tinydb import TinyDB, Query
player_database = TinyDB('models/players.json')

from models import player_model


class CreatePlayerController:
    def __init__(self):
        self.player_values = []
        # self.birthdate_list = []

    def __call__(self):
        last_name = input("Veuillez entrer le nom de famille :")
        last_name = self.validate_string(last_name)
        self.player_values.append(last_name)

        first_name = input("Veuillez entrer le prénom :")
        first_name = self.validate_string(first_name)
        self.player_values.append(first_name)
        self.player_values.append(self.prompt_for_add_birth_details())
        
        
        #player_database.insert({"Nom de famille" : last_name})
        print(self.player_values)

    def validate_string(self, string_to_check):
            string_valid = False
            while not string_valid:
                if string_to_check == "":
                    print("Le champs ne doit pas être vide")
                else :
                    string_valid = True
                    string_validated = string_to_check.upper()
                    return string_validated

    def prompt_for_add_birth_details(self):
        birthdate_list = []

        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance: ")
            if self.birth_day.isdigit() == True and len(self.birth_day) == 2 and int(self.birth_day) < 32:
                valid_day = True
                birthdate_list.append(self.birth_day)
            else: 
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                        
        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance: (En chiffre) ")
            if self.birth_month.isdigit() == True and len(self.birth_month) == 2 and int(self.birth_month) < 13:
                valid_month = True
                birthdate_list.append(self.birth_month)
            else:
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        valid_year = False
        while not valid_year:       
            self.birth_year = input("Entrez l'année de naissance: ")
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4 and int(self.birth_year) < 2021:
                valid_year = True
                birthdate_list.append(self.birth_year)
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980)")

        return f"{birthdate_list[0]}/{birthdate_list[1]}/{birthdate_list[2]}"





   

   