from tinydb import TinyDB

from views import view_main


tournament_database = TinyDB('models/tournament.json')


class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                 location=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players_ids=None,
                 list_of_tours=[],
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n\n {self.list_of_tours}\n"

    def serialized(self):
        tournament_infos = {}
        tournament_infos['Nom du tournoi'] = self.tournament_name
        tournament_infos['Lieu'] = self.location
        tournament_infos['Date'] = self.tournament_date
        tournament_infos['Nombre de tours'] = self.number_of_tours
        tournament_infos['Controle du temps'] = self.time_control
        tournament_infos['Description'] = self.description
        tournament_infos["Joueurs_id"] = self.players_ids
        tournament_infos["Tours"] = self.list_of_tours
        tournament_infos["Id du tournoi"] = self.tournament_id

        return tournament_infos

    def unserialized(self, serialized_tournament):
        tournament_name = serialized_tournament['Nom du tournoi']
        location = serialized_tournament['Lieu']
        tournament_date = serialized_tournament['Date']
        number_of_tours = serialized_tournament['Nombre de tours']
        time_control = serialized_tournament['Controle du temps']
        description = serialized_tournament['Description']
        players_ids = serialized_tournament["Joueurs_id"]
        list_of_tours = serialized_tournament["Tours"]
        tournament_id = serialized_tournament["Id du tournoi"]

        return Tournament(tournament_name,
                          location,
                          tournament_date,
                          number_of_tours,
                          time_control,
                          description,
                          players_ids,
                          list_of_tours,
                          tournament_id
                          )

    def add_to_database(self, tournament_values):
        tournament = Tournament(tournament_values[0],
                                tournament_values[1],
                                tournament_values[2],
                                tournament_values[3],
                                tournament_values[4],
                                tournament_values[5],
                                tournament_values[6],
                                )
        tournament_id = tournament_database.insert(tournament.serialized())
        tournament_database.update({"Id du tournoi": tournament_id}, doc_ids=[tournament_id])


class Tour:
    """
    Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs
    avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé,
    le gestionnaire du tournoi saisit les résultats de chaque match avant de
    générer les paires suivantes.
    Les instances de tour doivent être stockées dans une liste sur l'instance
    de tournoi à laquelle elles appartiennent.
    ---
    Renvoi l'instance de tour
    """

    # TOUR_NUMBER = 1

    def __init__(self, name=None, begin_time=None, end_time=None, list_of_finished_matchs=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_of_finished_matchs = list_of_finished_matchs
        self.list_of_tours = []

    def serialized(self):
        tour_infos = {}
        tour_infos['Nom'] = self.name
        tour_infos['Debut'] = self.begin_time
        tour_infos['Fin'] = self.end_time
        tour_infos['Matchs'] = self.list_of_finished_matchs
        return tour_infos

    def unserialized(self, serialized_tour):
        name = serialized_tour['Nom']
        begin_time = serialized_tour['Debut']
        end_time = serialized_tour['Fin']
        list_of_finished_matchs = serialized_tour['Matchs']
        return Tour(name,
                    begin_time,
                    end_time,
                    list_of_finished_matchs
                    )

    def __repr__(self):
        return f"{self.name} - Début : {self.begin_time}. Fin : {self.end_time}."

    def run(self, sorted_players_list, tournament_object):
        self.view = view_main.TourDisplay()
        self.list_of_tours = []
        self.list_of_finished_matchs = []
        self.name = "Tour " + str(len(tournament_object.list_of_tours) + 1)
        # Tour.TOUR_NUMBER += 1

        self.begin_time, self.end_time = self.view.display_tournament_time()

        # tant qu'il y a des joueurs dans la liste, ajoute des instances de 'match' dans la liste 'list_of_tours'
        while len(sorted_players_list) > 0:
            match_instance = Match(self.name, sorted_players_list[0], sorted_players_list[1])
            Match.MATCH_NUMBER += 1
            self.list_of_tours.append(match_instance)
            del sorted_players_list[0:2]

        self.view.display_tour(self.name, self.list_of_tours)

        for match in self.list_of_tours:

            valid_score_player_1 = False
            while not valid_score_player_1:
                try:
                    score_player_1 = input(f"Entrez le score de {match.player_1} :")
                    float(score_player_1)
                except Exception:
                    print("Vous devez entrer 0, 0.5, ou 1")
                else:
                    match.score_player_1 = float(score_player_1)
                    match.player_1.tournament_score += float(score_player_1)
                    valid_score_player_1 = True

            valid_score_player_2 = False
            while not valid_score_player_2:
                try:
                    score_player_2 = input(f"Entrez le score de {match.player_2} :")
                    float(score_player_2)
                except Exception:
                    print("Vous devez entrer 0, 0.5, ou 1")
                else:
                    match.score_player_2 = float(score_player_2)
                    match.player_2.tournament_score += float(score_player_2)
                    valid_score_player_2 = True

            self.list_of_finished_matchs.append(([match.player_1.player_id, match.score_player_1],
                                                 [match.player_2.player_id, match.score_player_2]))

        return Tour(self.name, self.begin_time, self.end_time, self.list_of_finished_matchs)


class Match:
    """
    Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
    chacune contenant deux éléments : une référence à une instance de joueur et un score.
    Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
    """

    MATCH_NUMBER = 1

    def __init__(self, name=None, player_1=None, player_2=None, score_player_1=0, score_player_2=0):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}."
