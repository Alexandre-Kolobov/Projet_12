import datetime
from os import system, name
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm, Prompt


class ViewEvenement():
    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def entrer_date_debut_evenement() -> datetime.date:
            while True:
                print("----------------------------------------")
                try:
                    date = input("Entrer la date de debut de l'evenement DD/MM/YYYY hh:mm:ss : ").strip()
                    date_format = "%d/%m/%Y %H:%M:%S"
                    if not datetime.datetime.strptime(date, date_format):
                        raise ValueError("la date doit être au format DD/MM/YYYY hh:mm:ss")
                    break

                except ValueError as exc:
                    print("Erreur: " + str(exc))

            return date

    @staticmethod
    def entrer_date_fin_evenement() -> datetime.date:
            while True:
                print("----------------------------------------")
                try:
                    date = input("Entrer la date de fin de l'evenement DD/MM/YYYY hh:mm:ss : ").strip()
                    date_format = "%d/%m/%Y %H:%M:%S"
                    if not datetime.datetime.strptime(date, date_format):
                        raise ValueError("la date doit être au format DD/MM/YYYY hh:mm:ss")
                    break

                except ValueError as exc:
                    print("Erreur: " + str(exc))

            return date


    @staticmethod
    def entrer_pays_evenement() -> str:
        while True:
            print("----------------------------------------")
            try:
                pays = input("Entrer le pays de l'evenement: ").strip()
                if not pays.isalpha() or pays == "":
                    raise ValueError("Le pays de l'evenement doit contenir que des lettres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return pays


    @staticmethod
    def entrer_ville_evenement() -> str:
        while True:
            print("----------------------------------------")
            try:
                ville = input("Entrer la ville de l'evenement: ").strip()
                if not ville.isalpha() or ville == "":
                    raise ValueError("La ville de l'evenement doit contenir que des lettres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return ville


    @staticmethod
    def entrer_rue_evenement() -> str:
        while True:
            print("----------------------------------------")
            try:
                rue = input("Entrer la rue de l'evenement: ").strip()
                if not rue.isalpha() or rue == "":
                    raise ValueError("La rue de l'evenement doit contenir que des lettres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return rue
    

    @staticmethod
    def entrer_numero_rue_evenement() -> int:
        while True:
            print("----------------------------------------")
            try:
                numero_rue = input("Entrer le numero de rue de l'evenement: ").strip()
                if not numero_rue.isnumeric() or numero_rue == "":
                    raise ValueError("Le numero de rue doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return numero_rue
    
    @staticmethod
    def entrer_cp_evenement() -> int:
        while True:
            print("----------------------------------------")
            try:
                cp = input("Entrer le code postal de l'evenement: ").strip()
                if not cp.isnumeric() or cp == "":
                    raise ValueError("Le code postal doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return cp


    @staticmethod
    def entrer_attendees_evenement() -> int:
        while True:
            print("----------------------------------------")
            try:
                cp = input("Entrer le nombre d'attendees pour l'evenement: ").strip()
                if not cp.isnumeric() or cp == "":
                    raise ValueError("Le nombre d'attendees doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return cp


    @staticmethod
    def entrer_notes_evenement() -> str:
        print("----------------------------------------")
        note = input("Entrer une note pour l'evenement: ")
        return note


    @staticmethod
    def entrer_contrat_id_evenement() -> int:
        while True:
            print("----------------------------------------")
            try:
                id_contrat = input("Entrer l'id du contrat de l'evenement: ").strip()
                if not id_contrat.isnumeric() or id_contrat == "":
                    raise ValueError("L'id du contrat doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_contrat


    @staticmethod
    def choisir_collaborateur_id(collaborateur_as_list_of_dict:list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le support à assigner pour cet événement:")

            keys = {}
            i = 1
            for collaborateur in collaborateur_as_list_of_dict:
                for key, value in collaborateur.items():
                    keys[i] = key
                    print(f"{i} - {value}")
                    i += 1 
            
            try:
                choix_collaborateur = input("Entrez le numéro du support: ").strip()
                
                if not choix_collaborateur.isnumeric() or choix_collaborateur == "":
                    raise ValueError("Merci de choisir parmis les supports proposés")
                
                if not int(choix_collaborateur) in range(1, i):
                    raise ValueError("Merci de choisir parmis les supports proposés")
                
                choix_collaborateur = keys[int(choix_collaborateur)]
                break

            except ValueError as exc:
                print("Erreur: " + str(exc))

        return choix_collaborateur


    @staticmethod
    def modifier_caracteristique(key:str, value:[str,int]) -> bool:
        while True:
            reponse = input(f"Voulez vous modifier {key}:{value}? [y/n]")
            if reponse.lower() == "y":
                return True
            
            if reponse.lower() == "n":
                return False
            
            print("Merci d'utiliser y or n")


    @staticmethod
    def afficher_evenements(list_evenements: list):
        ViewEvenement.clear()
        table = Table(title="List des événements")

        table.add_column("id", style="cyan", no_wrap=True)
        table.add_column("Date début", style="magenta")
        table.add_column("Date fin", style="magenta")
        table.add_column("Pays", style="magenta")
        table.add_column("Ville", style="magenta")
        table.add_column("Rue", style="magenta")
        table.add_column("N° Rue",justify="right", style="magenta")
        table.add_column("CP",justify="right", style="magenta")
        table.add_column("Attendees",justify="right", style="magenta")
        table.add_column("Notes", style="magenta")
        table.add_column("Contrat id", justify="right", style="magenta")
        table.add_column("Client", style="yellow")
        table.add_column("Commercial", style="green")
        table.add_column("Support id", justify="right", style="blue")
        table.add_column("Support", style="blue")

        for evenement in list_evenements:
            table.add_row(
                str(evenement.id),
                str(evenement.date_debut),
                str(evenement.date_fin),
                str(evenement.location_pays),
                str(evenement.location_ville),
                str(evenement.location_rue),
                str(evenement.location_num_rue),
                str(evenement.location_cp),
                str(evenement.attendees),
                str(evenement.notes),
                str(evenement.contrat_id),
                f"{evenement.contrat.client.nom} {evenement.contrat.client.prenom}",
                f"{evenement.contrat.collaborateur.nom} {evenement.contrat.collaborateur.prenom}" if evenement.contrat.collaborateur else "",
                str(evenement.collaborateur_id),
                f"{evenement.collaborateur.nom} {evenement.collaborateur.prenom}" if evenement.collaborateur else ""
                )


        console = Console()
        console.print(table)

    @staticmethod
    def redemander_ajouter_evenement() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous ajouter un autre evenement?")
        return reponse
    
    
    @staticmethod
    def demander_id_de_evenement_a_modifier() -> str:
        """Renvoi l'id de l'evenement à modifier"""
        while True:
            print("----------------------------------------")
            try:
                id_evenement = input("Indiquer l'id de l'événement à modifier:").strip()
                if not id_evenement.isnumeric() or id_evenement == "":
                    raise ValueError("L'id de l'événement doit être numerique et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_evenement
    
    
    @staticmethod
    def evenement_avec_id_nexiste_pas(id:str) -> None:
        print("----------------------------------------")
        print(f"Evenement avec id {id} n'existe pas")


    @staticmethod
    def redemander_modifier_un_autre_evenement() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous modifier un autre evenement?")
        return reponse
    

    @staticmethod
    def demander_id_evenement_a_supprimer() -> str:
        while True:
            print("----------------------------------------")
            try:
                id_evenement = input("Indiquer l'id de l'événement à supprimer:").strip()
                if not id_evenement.isnumeric() or id_evenement == "":
                    raise ValueError("L'id de l'événement doit être numerique et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_evenement
    

    @staticmethod
    def demander_de_confirmer_suppression_evenement(evenement) -> None:
        print("----------------------------------------")
        reponse = Confirm.ask(
            "Confirmer la suppression de l'évenement - "
            f"id{evenement.id}"
            )
        return reponse