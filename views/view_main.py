
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


class DisplayMenu:
    """Display the menu choosen by the user"""
    def __call__(self, menu_dict):
        for key in menu_dict:
            print(f"{key} : {menu_dict[key]}")
        print()


class GetUserChoiceInMenu:
    """Ask user to choose in a menu"""
    def __call__(self, menu_dict_choosen):
        valid_choice = False
        while not valid_choice:
            choice = input("--> ")
            if choice in menu_dict_choosen:
                valid_choice = True
                print(menu_dict_choosen[choice])
            else:
                print("Vous devez entrer le chiffre correspondant au menu")
        return choice