import sys

from views import view_main
from controllers import create_menus
from controllers import player_controller
from controllers import tournament_controller
from models import player_model


class HomeMenuController:
    """Display the title and leads to the main menu"""

    def __init__(self):
        self.view = view_main.MainDisplay()
        self.clear = view_main.ClearScreen()
        self.create_menu = create_menus.CreateMenus()
        self.choosen_controller = None

    def __call__(self):
        self.clear()
        self.view.display_title()
        entry = self.create_menu(self.create_menu.main_menu)

        if entry == "1":
            self.choosen_controller = PlayerMenuController()
            self.go_to_player_menu_controller()
        if entry == "2":
            self.choosen_controller = TournamentMenuController()
            self.go_to_tournament_menu_controller()
        if entry == "3":
            self.choosen_controller = QuitAppController()
            self.go_to_quit_app_controller()

    def go_to_player_menu_controller(self):
        return self.choosen_controller()

    def go_to_tournament_menu_controller(self):
        return self.choosen_controller()

    def go_to_quit_app_controller(self):
        return self.choosen_controller()


class PlayerMenuController(HomeMenuController):

    def __init__(self):
        super().__init__()
        self.create_player = player_controller.CreatePlayerController()
        self.players_report = player_controller.PlayerReport()
        self.home_menu_controller = HomeMenuController()
        self.player_model = player_model.Player()

    def __call__(self):
        entry = self.create_menu(self.create_menu.player_menu)
        if entry == "1":
            self.choosen_controller = self.create_player()
        if entry == "2":
            self.choosen_controller = self.player_model.update_ranking()
        if entry == "3":
            self.choosen_controller = self.players_report()
        if entry == "4":
            self.choosen_controller = self.home_menu_controller()


class TournamentMenuController(HomeMenuController):

    def __init__(self):
        super().__init__()
        self.tournament_report_controller = tournament_controller.TournamentReport()
        self.create_tournament = tournament_controller.CreateTournamentController()
        self.home_menu_controller = HomeMenuController()
        self.start_tournament = tournament_controller.StartTournament()

    def __call__(self):
        entry = self.create_menu(self.create_menu.tournament_menu)
        if entry == "1":
            self.choosen_controller = self.create_tournament()
        if entry == "2":
            self.choosen_controller = self.start_tournament()
        if entry == "3":
            self.choosen_controller = self.start_tournament.load_tournament_statement()
        if entry == "4":
            self.choosen_controller = self.tournament_report_controller()
        if entry == "5":
            self.choosen_controller = self.home_menu_controller()


class QuitAppController:

    def __call__(self):
        sys.exit()
