# from controllers import create_menus
from views import view_main


class ApplicationController:
    def __init__(self):
        self.controller = None
    
    def start(self):
        self.controller = HomeMenuController()
        self.controller()
        # while self.controller:
        #     self.controller = self.controller()


class HomeMenuController:
    def __init__(self):
        self.view = view_main.MainMenuDisplay()
        self.create_menu = CreateMenus()

    def __call__(self):
        self.view.display_title()
        self.create_menu(self.create_menu.main_menu)


class PlayerMenuController(HomeMenuController):
    def __call__(self):
        self.create_menu(self.create_menu.play_menu)


class TournamentMenuController(HomeMenuController):
    def __call__(self):
        return print("Dans le TournamentMenuController")


class QuitAppController:
    pass


class CreateMenus():
    """Crée un menu a partir d'une liste et l'affiche"""
    
    def __init__(self):
        self.main_menu = [("1", "Menu Joueur", "PlayerMenuController()"),
        ("2", "Menu Tournoi", "TournamentMenuController()"),
        ("3", "Quitter", "QuitAppController()")]

        self.play_menu = [("1", "Ajouter un joueur à la base", "QuitAppController()"),
        ("2", "Mettre à jour le classement d'un joueur"),
        ("3", "Retour au menu principal")]

    def __call__(self, menu_to_display):
        for line in menu_to_display:
            print(line[0] + " : "+ line[1])
        while True:
            entry = input("-->")
            for line in menu_to_display:
                if entry == line[0]:
                    return line[2]
            print("Vous devez entrer le chiffre correspondant")
        

