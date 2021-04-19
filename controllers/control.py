from views import view_main
from views import menus
from views import player
from controllers import control_player


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
        # Show the main title
        self.view.display_title() 

        # Show the main menu
        self.display_menu(self.menu.main_menu_dict) 

        # Ask and return the user's choice
        entry = self.get_user_choice(self.menu.main_menu_dict)  
        
        self.link_to_menu(entry)

    def link_to_menu(self, entry): 
        self.player_menu_controller = PlayerMenuController()
        self.tournament_menu_controller = TournamentMenuController()
        self.quit_app_controller = QuitAppController()
        self.report_menu_controller = ReportMenuController()
        
        if entry == "1":
            self.player_menu_controller.run()
        if entry == "2":
            self.tournament_menu_controller.run()
        if entry == "3":
            self.report_menu_controller.run()
        if entry == "4":
            self.quit_app_controller.run()



class TournamentMenuController:
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    def run(self):
        self.display_menu(self.menu.tournament_root_menu_dict)


class ReportMenuController:
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    def run(self):
        self.display_menu(self.menu.report_root_menu_dict)


class QuitAppController:
    def run(self):
        pass
