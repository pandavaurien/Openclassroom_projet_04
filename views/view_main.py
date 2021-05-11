import datetime
from os import system, name
import pandas as pd

from models import tournament_model



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
              "------------------------------------------------\n"
              )
    


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


class TourDisplay:
    """Docstring"""
    def __init__(self):
        self.round = tournament_model.Round() 
    
    def display_tour(self, tour_name, list_of_rounds):
        """Display the tour at the beginning of it"""
        
        print(f"--------------------------{tour_name}-------------------------\n")
        for round in list_of_rounds:
            print(round.__str__())
        print()

    def display_tournament_time(self):

        print()
        input("Appuyez sur une touche pour commencer le tour")
        print()
        begin_time = datetime.datetime.now()
        print(f"Début du tour : {begin_time}")
        print()
        input("Appuyez sur une touche lorsque le tour est terminé")
        print()
        end_time = datetime.datetime.now()
        print(f"Fin du tour : {end_time}")
        print()
        return begin_time, end_time



class EndTournamentDisplay:
    """Display the final score at the end of the tournament"""
    def __call__(self, tournament_instance, players_instance_list):
        print("------------------------------------------------\n"
              "-----------------Fin du tournoi-----------------\n"
              "------------------------------------------------\n"
              "-------------------Résultats--------------------\n"
              "------------------------------------------------\n")
        for i in tournament_instance.list_of_players:
            print(i)
        print(players_instance_list)
        print(tournament_instance)