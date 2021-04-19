from models import menus


class MainMenuDisplay:
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
              "------------------------------------------------\n")             

    # def get_user_choice(self):
    #     """Ask user to choose a menu in the main menu"""
    #     valid_choice = False
    #     while not valid_choice:
    #         choice = input("--> ")
    #         if choice == "1":
    #             valid_choice = True
    #         elif choice == "2":
    #             valid_choice = True
    #         elif choice == "3":
    #             valid_choice = True
    #         else:
    #             print("Vous devez entrer 1, 2 ou 3")
    #     return choice


class DisplayMenu:
    """Display the menu choosen by the user"""
    def __call__(self, menu_dict):
        for key in menu_dict:
            print(f"{key} : {menu_dict[key]}")
        print()


class GetUserChoiceInMenu:
    """Ask user to choose a menu in the main menu"""
    def __call__(self, menu_dict_choosen):
        self.menu_dict_choosen = menu_dict_choosen

        valid_choice = False
        while not valid_choice:
            choice = input("--> ")
            if choice == menu_dict_choosen[choice]:
                valid_choice = True
            else:
                print("Vous devez entrer le chiffre correspondant au menu")
        return menu_dict_choosen[choice]