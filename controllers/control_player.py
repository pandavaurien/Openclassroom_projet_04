from views import view_main
from views import menus
from views import player



class PlayerMenuController:
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    def run(self):
        self.display_menu(self.menu.player_root_menu_dict)


class CreatePlayerController:
    create_player = player.ViewAddPlayer()
    get_user_choice = view_main.GetUserChoiceInMenu()
    display_menu = view_main.DisplayMenu()
    menu = menus.Menus()
    
    def run(self):
        self.create_player.prompt_for_add_last_name()
        entry = self.get_user_choice(self.player_root_menu_dict)
        self.link_to_menu(entry)

    def link_to_menu(self, entry): 
        self.player_menu_controller = control.PlayerMenuController()
        self.tournament_menu_controller = control.TournamentMenuController()
        self.home_menu_controller = control.HomeMenuController()
        
        
        if entry == "1":
            self.player_menu_controller.run()
        if entry == "2":
            self.tournament_menu_controller.run()
        if entry == "3":
            self.report_menu_controller.run()
        if entry == "4":
            self.quit_app_controller.run()