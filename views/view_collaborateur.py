from os import system, name
import getpass
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm

class ViewCollaborateur():
    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


    @staticmethod
    def entrer_prenom_collaborateur() -> str:
            while True:
                print("----------------------------------------")
                try:
                    prenom = input("Entrer le prénom du collaborateur: ").strip()
                    if not prenom.isalpha() or prenom == "":
                        raise ValueError("Le prénom du collaborateur doit contenir que des lettres et ne pas être vide")
                    break
                except ValueError as exc:
                    print("Erreur: " + str(exc))

            return prenom


    @staticmethod
    def entrer_nom_collaborateur() -> str:
        while True:
            print("----------------------------------------")
            try:
                nom = input("Entrer le nom du collaborateur: ").strip()
                if not nom.isalpha() or nom == "":
                    raise ValueError("Le nom du collaborateur doit contenir que des lettres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return nom
    

    @staticmethod
    def entrer_email_collaborateur() -> str:
        while True:
            print("----------------------------------------")
            try:
                email = input("Entrer l'email du collaborateur: ").strip()
                if email == "":
                    raise ValueError("L'email du collaborateur ne doit pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return email


    @staticmethod
    def entrer_telephone_collaborateur() -> int:
        while True:
            print("----------------------------------------")
            try:
                telephone = input("Entrer le numero telephone du collaborateur: ").strip()
                if not telephone.isnumeric() or telephone == "":
                    raise ValueError("Le numero telephone doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return telephone
    

    @staticmethod
    def entrer_mot_de_passe_collaborateur() -> str:
        while True:
            print("----------------------------------------")
            try:
                mot_de_passe = getpass.getpass("Entrer le mot de passe du collaborateur: ").strip()
                if mot_de_passe == "":
                    raise ValueError("Le mot de passe ne doit pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return mot_de_passe


    @staticmethod
    def choisir_role_collaborateur(roles_as_list_of_dict:list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le role pour ce collaborateur:")
            for role in roles_as_list_of_dict:
                for key, value in role.items():
                    print(f"{key} - {value}")
            
            choix_role = input("Entrer le numero du role: ").strip()
            choix_role = int(choix_role)

            for role in roles_as_list_of_dict:
                if choix_role in role.keys():
                    return choix_role
            
            print("Merci de choisir parmis les roles proposés")


    @staticmethod
    def refuser_authentification():
        print("----------------------------------------")
        print("Les informations d'identification ne sont pas correctes")
        print("Merci de reesayer")


    @staticmethod
    def refuser_token():
        print("----------------------------------------")
        print("Le token n'est pas correcte")


    @staticmethod
    def refuser_permissions():
        print("----------------------------------------")
        print("Vous n'avez pas de permission pour réaliser cette action")

    
    @staticmethod
    def modifier_caracteristique(key:str, value:[str,int]) -> bool:
        while True:
            print("----------------------------------------")
            reponse = input(f"Voulez vous modifier {key}:{value}? [y/n]")
            if reponse.lower() == "y":
                return True
            
            if reponse.lower() == "n":
                return False
            
            print("Merci d'utiliser y or n")

    @staticmethod
    def initialisation_collaborateur() -> None:
        print("----------------------------------------")
        print("Pour le premiere lancement de l'application nous devons créer un utilisateur gestionnaire.")


    @staticmethod
    def afficher_collaborateurs(list_collaborateur: list):
        ViewCollaborateur.clear()
        table = Table(title="List des collaborateurs")

        table.add_column("id", style="cyan", no_wrap=True)
        table.add_column("Nom Prenom", style="magenta")
        table.add_column("Email", style="magenta")
        table.add_column("Telephone", style="magenta")
        table.add_column("Role id", justify="right", style="green")
        table.add_column("Role name", style="green")

        for collaborateur in list_collaborateur:
            table.add_row(
                str(collaborateur.id),
                f"{collaborateur.prenom} {collaborateur.nom}",
                str(collaborateur.email),
                str(collaborateur.telephone),
                str(collaborateur.role_id),
                str(collaborateur.role.role_name)
                )


        console = Console()
        console.print(table)

    @staticmethod
    def confirmation_ajout_collaborateur(collaborateur) -> None:
        print("----------------------------------------")
        print(f"Le collaborateur {collaborateur.nom} {collaborateur.prenom} a été ajouté")


    @staticmethod
    def redemander_ajouter_collaborateur() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous ajouter un autre collaborateur?")
        return reponse
    
    @staticmethod
    def demander_id_du_collaborateur_a_modifier() -> str:
        print("----------------------------------------")
        id_collaborateur = input("Indiquer l'id du collaborateur à modifier:")
        return id_collaborateur
    
    @staticmethod
    def demander_id_du_collaborateur_a_supprimer() -> str:
        print("----------------------------------------")
        id_collaborateur = input("Indiquer l'id du collaborateur à supprimer:")
        return id_collaborateur
    
    @staticmethod
    def demander_de_modifier_un_autre_collaborateur() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous modifier un autre collaborateur?")
        return reponse
    
    @staticmethod
    def demander_authentification() -> None:
        print("----------------------------------------")
        print("Entrer votre email et mot de passe pour se connecter")


    @staticmethod
    def demander_de_confirmer_suppression_collaborateur(collaborateur) -> None:
        print("----------------------------------------")
        reponse = Confirm.ask(
            "Confirmer la suppression du collaborateur - "
            f"id{collaborateur.id} {collaborateur.nom} {collaborateur.prenom}"
            )
        return reponse