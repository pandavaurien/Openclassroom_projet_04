import time
from os import system, name
import pandas as pd

from models import player_model, tournament_model


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

    def display_datas_in_a_frame(self, data, index=None, columns=None):
        display = pd.DataFrame(self, data, index, columns)
        print()
        print("Voici les données que vous avez entrer :")
        print()
        print(display)
        print()


class TournamentDisplay:
    """Display the tournament details if it's not already played"""

    def __call__(self):
        tournaments_database = tournament_model.tournament_database
                        
        for tournament in tournaments_database:
            if tournament['Tours'] == []:
                print(f"{tournament.doc_id} - Nom: {tournament['Nom du tournoi']} - Lieu: {tournament['Lieu']}")


class PlayersDiplay:
    """Display all the players in the database"""

    def __call__(self):
        players_database = player_model.player_database

        for player in players_database:
            print(f"{player.doc_id} - {player['Nom']} {player['Prenom']} - Classement : {player['Classement']}")


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
        begin_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Début du tour : {begin_time}")
        print()
        input("Appuyez sur une touche lorsque le tour est terminé")
        print()
        end_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Fin du tour : {end_time}")
        print()
        return begin_time, end_time


class EndTournamentDisplay:
    """Display the final score at the end of the tournament"""
    def __call__(self, tournament_instance): #TODO Afficher les noms à la place des ids dans les résultats
        print("------------------------------------------------\n"
              "-----------------Fin du tournoi-----------------\n"
              "------------------------------------------------\n"
              "-------------------Résultats--------------------\n"
              "------------------------------------------------\n")
       
        print(tournament_instance)


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
        input("Appuyez sur une touche pour revenir au menu principal")

    def choose_a_tournament(self):
        print(pd.read_json("models/tournament.json"))


class AskForContinuingTournament:
    def __call__(self, choice):
        print("Voulez vous sauvegarder et quitter le tournoi en cours ? Y / N")
        valid_choice = True
        while valid_choice:
            choice = input("--->")
            if choice == 'Y':
                break
            if choice == 'N':
                self


