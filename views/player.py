from models import players

class ViewAddPlayer:
    """Class displaying the views when a user add a player"""
    to_player_model = players.Player()

    def prompt_for_add_last_name(self):
        valid_last_name = False
        while not valid_last_name:
            last_name = input("Entrez le nom de famille: ")
            if last_name != "":
                valid_last_name = True
            else:
                print("Vous devez entrer un nom")
        return last_name
        
    def prompt_for_add_first_name(self):
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Entrez le prénom: ")
            if first_name != "":
                valid_first_name = True
            else:
                print("Vous devez entrer un prénom ")
        return first_name
    
    def prompt_for_add_birth_details(self):
        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance: ") # erreur si il n'y a pas de "self"
            if self.birth_day.isdigit() == True and len(self.birth_day) == 2 and int(self.birth_day) < 32:
                valid_day = True
            else: 
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                        
        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance: (En chiffre) ")
            if self.birth_month.isdigit() == True and len(self.birth_month) == 2 and int(self.birth_month) < 13:
                valid_month = True
            else:
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        valid_year = False
        while not valid_year:       
            self.birth_year = input("Entrez l'année de naissance: ")
            if self.birth_year.isdigit() == True and len(self.birth_year) == 4 and int(self.birth_year) < 2021:
                valid_year = True
            else:
                print("Veuillez entrer une année à 4 chiffres (exemple : 1980)")
        
        return self.to_player_model.birthdate_list.append(self.birth_day), 
        self.to_player_model.birthdate_list.append(self.birth_month),
        self.to_player_model.birthdate_list.append(self.birth_year)

    def prompt_for_gender(self):
        valid_gender = False
        while not valid_gender:
            gender = input("Choisissez le genre du joueur \n'H' pour un homme \n'F' pour une femme: ")
            if gender == "H":
                valid_gender = True
                return "Homme"
            elif gender == "F":
                valid_gender = True
                return "Femme"
            else:
                print("Vous devez entrer un genre (H ou F)")
 
    def prompt_for_ranking(self):
        valid_ranking = False
        while not valid_ranking:
            ranking = input("Entrez le classement du joueur: ")
            if ranking.isdigit() == True and int(ranking) >= 0:
                valid_ranking = True
            else :
                print("Vous devez entrer un nombre entier positif")
        return ranking
