import datetime
from os import system, name
from numpy import format_float_positional
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
        self.match = tournament_model.Match() 
    
    def display_tour(self, tour_name, list_of_matchs):
        """Display the tour at the beginning of it"""
        
        print(f"--------------------------{tour_name}-------------------------\n")
        print()
        for match in list_of_matchs:
            print(match)
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
    def __call__(self, tournament_instance):
        print("------------------------------------------------\n"
              "-----------------Fin du tournoi-----------------\n"
              "------------------------------------------------\n"
              "-------------------Résultats--------------------\n"
              "------------------------------------------------\n")
       
        print(tournament_instance)

        # for tour in tournament_instance.list_of_tours:
        #     print(f"{tournament_instance.list_of_tours.begin_time} {tournament_instance.list_of_tours.end_time}")
        # for rnds in tournament_instance.tour.list_of_finished_matchs:
        #         print(rnds)
                # print(f"{tour.list_of_finished_matchs[0][0]} ---CONTRE--- {tour.list_of_finished_matchs[0][1]}")


class DisplayPlayersReport:

    def __call__(self):
        print("------------------------------------------------\n"
              "-------------Affichages des joueurs-------------\n"
              "------------------------------------------------\n"
              " Afficher les rapports :\n"
              )
        
    def display_alphabetical(self, players_list):
        for player in players_list:
            print(f"{player.last_name} {player.first_name} - {player.birthdate} - {player.gender} - Classement : {player.ranking}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()


    def display_ranking(self, players_list):
        for player in players_list:
            # player.ranking = int(player.ranking)
            print(f"Classement :{player.ranking} - {player.last_name} {player.first_name} - {player.birthdate} - {player.gender}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()


class DisplayTournamentsReport:

    def __call__(self):
            print("------------------------------------------------\n"
                  "--------------Rapport des tournois--------------\n"
                  "------------------------------------------------\n"
                  " Afficher les rapports :\n"
                  )

    def display_tournaments(self, tournaments_list, players_list):
        for tournament in tournaments_list:
            print(f"{tournament.tournament_name} - {tournament.location} - {tournament.tournament_date}\n"
                  f"Nombre de tours : {tournament.number_of_tours}\n"
                  f"Contrôle du temps : {tournament.time_control}\n"
                  f"Description : {tournament.description}\n"
                  )       
            for player in players_list:
                print(f"Joueurs : {player.last_name} - {player.first_name} - Classement : {player.ranking}")
            print()