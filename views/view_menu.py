from os import system, name
from enum import Enum
from rich.prompt import Confirm

class ViewMenu():
    choix_navigation =Enum("Choix",["COLLABORATEURS", "CLIENTS", "CONTRATS", "EVENEMENTS", "QUITTER"])
    choix_crud = Enum("Choix",["AFFICHER", "AJOUTER", "MODIFIER", "SUPPRIMER", "REVENIR", "QUITTER"])

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    
    @staticmethod
    def afficher_menu_principal() -> str:
        while True:
            
            print("----------------------------------------")
            print("1 - Collaborateurs")
            print("2 - Clients")
            print("3 - Contrats")
            print("4 - Evenements")
            print("5 - Quitter")
            print("----------------------------------------")

            choix = ViewMenu.choix_navigation
            values = [enum.value for enum in choix]
            choix_utilisateur = input("Merci de selectionner parmis les options proposées:").strip()

            if choix_utilisateur.isnumeric():
                choix_utilisateur = int(choix_utilisateur)

            if choix_utilisateur in values:
                return (choix(choix_utilisateur).name)
            else:
                ViewMenu.clear()
                print(f"Votre choix '{choix_utilisateur}' ne correspond pas aux choix proposés")


    @staticmethod
    def afficher_menu_model(model:str) -> str:
        # ViewMenu.clear()
        while True:
            
            print("----------------------------------------")
            print(f"1 - Afficher {model}s")
            print(f"2 - Ajouter {model}")
            print(f"3 - Modifier {model}")
            print(f"4 - Supprimer {model}")
            print(f"5 - Revenir dans le menu principal")
            print(f"6 - Quitter")
            print(f"----------------------------------------")

            choix = ViewMenu.choix_crud
            values = [enum.value for enum in choix]
            choix_utilisateur = input("Merci de selectionner parmis les options proposées:").strip()

            if choix_utilisateur.isnumeric():
                choix_utilisateur = int(choix_utilisateur)

            if choix_utilisateur in values:
                return (choix(choix_utilisateur).name)
            else:
                ViewMenu.clear()
                print(f"Votre choix '{choix_utilisateur}' ne correspond pas aux choix proposés")


    @staticmethod
    def revenir_a_ecran_precedent():
        reponse = Confirm.ask("Voulez vous revenir dans le menu des collaborateurs?")
        return reponse
    
