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
        
        print(f"---------------{tour_name}---------------")
        for round in list_of_rounds:
            print(round.__str__())
        print()

    # Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_rounds)
    # self.list_of_finished_rounds.append(([round.player_1, score_player_1], [round.player_2, score_player_2]))

    # def display_score(self, tour_instance):
    #     print(f"---------------{tour_instance.name}---------------\n"
    #           f"Heure de début : {tour_instance.begin_time}\n"
    #           f"Heure de fin : {tour_instance.end_time}\n")
    #     print(f"{tour_instance.list_of_finished_rounds}")

    #     for tple in tour_instance.list_of_finished_rounds:
    #         for lst in tple:
    #             print(lst[0], lst[1])

        

            


        
        
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


