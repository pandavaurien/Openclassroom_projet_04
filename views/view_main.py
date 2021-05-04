from os import system, name
import pandas as pd



class MainDisplay:
    """Docstring"""
   
    def display_title(self):
        """Display the title of the application"""
        print("------------------------------------------------\n"
              "---------------Gestion de tournoi---------------\n"
              "------------------------------------------------\n"
              "------------------------------------------------\n"
              "-----------------Menu principal-----------------\n"
              "------------------------------------------------\n"
              " Entrez le numéro correspondant au menu choisi :\n"
              "------------------------------------------------\n")
    

class ClearScreen:
    """Clear the terminal"""
    def __call__(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

  
class FrameDisplay:
    """Display the datas from a controller"""
    def __init__(self):
        pass

    def display_datas_in_a_frame(self, data, index=None, columns=None):
        display = pd.DataFrame(self, data, index, columns)
        print()
        print("Voici les données que vous avez entrer :")
        print()
        print(display)
        print()
        
        
# class PlayersDisplay:
#     """Display all the players"""
#     def __call__(self):
#         display_players_database = pd.read_json("models/players.json")
#         print(display_players_database)


# class TournamentDisplay:
#     """Display all the tournament"""
#     def __call__(self):
#         display_tournament_database = pd.read_json("models/players.json")
#         print(display_players_database)


