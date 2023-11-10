from os import system, name
from enum import Enum
from rich.console import Console
from rich.table import Table

class ViewMenu():
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
            ViewMenu.clear()
            print("----------------------------------------")
            print("1 - Consulter la base de données")
            print("2 - Créer/modifier dans la base de données")
            print("3 - Quitter")
            print("----------------------------------------")

            Choix = Enum("Choix",["Consulter", "Créer/modifier", "Quitter"])
            values = [enum.value for enum in Choix]
            choix_utilisateur = int(input("Merci de selectionner parmis les options proposées:"))

            if choix_utilisateur in values:
                return (Choix(choix_utilisateur).name)
            else:
                input("Merci de selectionner parmis les options proposées:")


    @staticmethod
    def afficher_collaborateurs(list_collaborateur: list):
        ViewMenu.clear()
        table = Table(title="List des collaborateurs")

        table.add_column("id", style="cyan", no_wrap=True)
        table.add_column("Nom Prenom", style="magenta")
        table.add_column("Role", justify="right", style="green")

        for collaborateur in list_collaborateur:
            table.add_row(str(collaborateur.id), f"{collaborateur.prenom} {collaborateur.nom}", str(collaborateur.role_id))


            console = Console()
            console.print(table)