from views import view_main
from models import menus



class ApplicationController:
    
    def start(self):
        self.controller = HomeMenuController()
        self.controller.run()


class HomeMenuController:
    view = view_main.MainMenuDisplay()
    get_user_choice = view_main.GetUserChoiceInMenu()
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    
    def run(self):
        self.view.display_title() # Show the main title
        self.display_menu(self.menu.main_menu_dict) # Show the main menu
        entry = self.get_user_choice(self.menu.main_menu_dict) # Prompt to choose 
        self.link_to_menu(entry)

    def link_to_menu(self, entry): 
        self.PMController = PlayerMenuController()
        self.TMController = TournamentMenuController()
        self.QAController = QuitAppController()
        if entry == "1":
            self.PMController.run()
        if entry == "2":
            self.TMController.run()
        if entry == "3":
            self.QAController.run()


class PlayerMenuController:
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    def run(self):
        self.display_menu(self.menu.player_root_menu_dict)
    

class TournamentMenuController:
    def run(self):
        print("dans le TournamentMenuController")


class QuitAppController:
    def run(self):
        pass