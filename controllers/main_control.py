from views import view_main
from controllers import create_menus
from controllers import create_player


class HomeMenuController:
    """Display the title and leads to the main menu"""
    
    def __init__(self):
        self.view = view_main.MainMenuDisplay()
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
    def __call__(self):
        entry = self.create_menu(self.create_menu.player_menu)
        if entry == "1":
            self.choosen_controller = self.create_player()

    def go_to_create_player_controller(self):
        return self.choosen_controller


class TournamentMenuController:
    def __call__(self):
        return print("Dans le TournamentMenuController")


class QuitAppController:
    def __call__(self):
        pass

