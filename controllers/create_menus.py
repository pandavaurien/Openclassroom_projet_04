# from controllers import main_control

# class CreateMenus:
#     _main_menu = [("1", "Menu Joueur", main_control.PlayerMenuController()),
#          ("2", "Menu Tournoi", main_control.TournamentMenuController()),
#           ("3", "Quitter", main_control.QuitAppController())]

#     # play_menu = [("1", "Ajouter un joueur à la base", control.QuitAppController()),
#     #     ("2", "Mettre à jour le classement d'un joueur"),
#     #     ("3", "Retour au menu principal")]

#     def __init__(self):
#         # self.player_menu_controller = control.PlayerMenuController()
#         pass
    
#     def __call__(self, menu_to_display):
#         for line in menu_to_display:
#             print(line[0] + " : "+ line[1])
#         while True:
#             entry = input("-->")
#             for line in menu_to_display:
#                 if entry == line[0]:
#                     return line[2]
#             print("Vous devez entrer le chiffre correspondant")