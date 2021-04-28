from views import view_main
from controllers import create_menus
from controllers import create_player
from controllers import tournament
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

    def __init__ (self):
        super().__init__()
        self.create_player = create_player.CreatePlayerController()
        self.home_menu_controller = HomeMenuController()
        self.player_model = player_model.Player()
    def __call__(self):
        entry = self.create_menu(self.create_menu.player_menu)
        if entry == "1":
            self.choosen_controller = self.create_player()
        if entry == "2":
            self.choosen_controller = self.player_model.update_ranking() 
        if entry == "3":
            pass
        if entry == "4":
            self.choosen_controller = self.home_menu_controller()


class TournamentMenuController(HomeMenuController):
    def __init__ (self):
        super().__init__()
        self.create_tournament = tournament.CreateTournamentController()
        self.home_menu_controller = HomeMenuController()
    def __call__(self):
        entry = self.create_menu(self.create_menu.tournament_menu)
        if entry == "1":
            self.choosen_controller = self.create_tournament()
        if entry == "2":
            pass
        if entry == "3":
            pass
        if entry == "4":
            self.choosen_controller = self.home_menu_controller()


class QuitAppController:
    def __call__(self):
        pass


class Function:
    def __init__(self):
        pass
    
    # Ne fonctionne pas 
    def check_if_digit(self):
        choice = input("-->")
        try:
            int(choice)
        except:
            print("\nVous devez entrer un nombre entier")
            self.check_if_digit()

        return int(choice)
        

    # def check_if_positive(self, number_to_check):
        
    #     if number_to_check <= 0:
    #             print("\nVous devez entrer un nombre entier")
    #     return number_to_check




