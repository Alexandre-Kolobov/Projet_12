from os import system, name
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm


class ViewContrat():
    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def entrer_montant_total() -> int:
        while True:
            print("----------------------------------------")
            try:
                montant = input("Entrer le montant total du contrat: ").strip()
                if not montant.isnumeric() or montant == "":
                    raise ValueError("Le montant du contrat doit être numerique et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return montant

    def entrer_reste_a_payer(montant_total: int) -> int:
        while True:
            print("----------------------------------------")
            try:
                reste = input("Entrer le reste a payer du contrat: ").strip()
                if not reste.isnumeric() or reste == "" or int(montant_total) < int(reste):
                    raise ValueError(
                        "Le reste a payer du contrat doit être numerique et ne pas être vide et être inférieur au montant total"
                        )
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return reste

    def choisir_statut() -> int:
        while True:
            print("----------------------------------------")

            reponse = input("Est-ce que contrat a été singé? [y/n] ").strip()
            if reponse.lower() == "y":
                return True

            if reponse.lower() == "n":
                return False

            print("Merci d'utiliser y or n")

    @staticmethod
    def choisir_client_id(clients_as_list_of_dict: list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le client à assigner pour ce contrat:")

            keys = {}
            i = 1
            for client in clients_as_list_of_dict:
                for key, value in client.items():
                    keys[i] = key
                    print(f"{i} - {value}")
                    i += 1

            try:
                choix_client = input("Entrez le numéro du client: ").strip()

                if not choix_client.isnumeric() or choix_client == "":
                    raise ValueError("Merci de choisir parmis les clients proposés")

                if not int(choix_client) in range(1, i):
                    raise ValueError("Merci de choisir parmis les clients proposés")

                choix_client = keys[int(choix_client)]
                break

            except ValueError as exc:
                print("Erreur: " + str(exc))

        return choix_client

    @staticmethod
    def choisir_collaborateur_id(collaborateur_as_list_of_dict: list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le collaborateur à assigner pour ce contrat:")
            keys = {}
            i = 1
            for collaborateur in collaborateur_as_list_of_dict:
                for key, value in collaborateur.items():
                    keys[i] = key
                    print(f"{i} - {value}")
                    i += 1

            try:
                choix_collaborateur = input("Entrer le numero du collaborateur: ").strip()

                if not choix_collaborateur.isnumeric() or choix_collaborateur == "":
                    raise ValueError("Merci de choisir parmis les collaborateurs proposés")

                if not int(choix_collaborateur) in range(1, i):
                    raise ValueError("Merci de choisir parmis les collaborateurs proposés")

                choix_collaborateur = keys[int(choix_collaborateur)]
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return choix_collaborateur

    @staticmethod
    def modifier_caracteristique(key: str, value: [str, int]) -> bool:
        while True:
            reponse = input(f"Voulez vous modifier {key}:{value}? [y/n]")
            if reponse.lower() == "y":
                return True

            if reponse.lower() == "n":
                return False

            print("Merci d'utiliser y or n")

    @staticmethod
    def afficher_contrats(list_contrats: list):
        ViewContrat.clear()
        table = Table(title="List des contrats")

        table.add_column("id", style="cyan", no_wrap=True)
        table.add_column("Montant Total", style="magenta")
        table.add_column("Reste à payer", style="magenta")
        table.add_column("Date de création", style="magenta")
        table.add_column("Statut", style="magenta")
        table.add_column("Commercial id", justify="right", style="green")
        table.add_column("Commercial Nom Prenom", style="green")
        table.add_column("Client id", justify="right", style="yellow")
        table.add_column("Client Nom Prenom", style="yellow")
        table.add_column("Client Entreprise", style="yellow")

        for contrat in list_contrats:
            table.add_row(
                str(contrat.id),
                str(contrat.montant_total),
                str(contrat.reste_a_payer),
                str(contrat.date_creation),
                str(contrat.statut_signe),
                str(contrat.collaborateur_id),
                f"{contrat.collaborateur.nom} {contrat.collaborateur.prenom}",
                str(contrat.client_id),
                f"{contrat.client.nom} {contrat.client.prenom}",
                f"{contrat.client.entreprise}"
            )

        console = Console()
        console.print(table)

    @staticmethod
    def redemander_ajouter_contrat() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous ajouter un autre contrat?")
        return reponse

    @staticmethod
    def redemander_modifier_un_autre_contrat() -> None:
        print("----------------------------------------")
        reponse = Confirm.ask("Voulez-vous modifier un autre contrat?")
        return reponse

    @staticmethod
    def demander_id_du_contrat_a_modifier() -> str:
        while True:
            print("----------------------------------------")
            try:
                id_contrat = input("Indiquer l'id du contrat à modifier:").strip()
                if not id_contrat.isnumeric() or id_contrat == "":
                    raise ValueError("L'id du contrat doit être numerique et ne pas être vide")
                break

            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_contrat

    @staticmethod
    def demander_id_du_contrat_a_supprimer() -> str:
        while True:
            print("----------------------------------------")
            try:
                id_contrat = input("Indiquer l'id du contrat à supprimer:").strip()
                if not id_contrat.isnumeric() or id_contrat == "":
                    raise ValueError("L'id du contrat doit être numerique et ne pas être vide")
                break

            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_contrat

    @staticmethod
    def contrat_avec_id_nexiste_pas(id: str) -> None:
        print("----------------------------------------")
        print(f"Contrat avec id {id} n'existe pas")

    @staticmethod
    def demander_de_confirmer_suppression_contrat(contrat) -> None:
        print("----------------------------------------")
        reponse = Confirm.ask(
            "Confirmer la suppression du contrat - "
            f"id{contrat.id}"
            )
        return reponse

    @staticmethod
    def demander_id_du_contrat_pour_evenement() -> str:
        while True:
            print("----------------------------------------")
            try:
                id_contrat = id_contrat = input("Indiquer l'id du contrat pour lequel vous voulez créer un événement:").strip()
                if not id_contrat.isnumeric() or id_contrat == "":
                    raise ValueError("L'id du contrat doit être numerique et ne pas être vide")
                break

            except ValueError as exc:
                print("Erreur: " + str(exc))

        return id_contrat

    @staticmethod
    def contrat_avec_id_nest_pas_signe() -> None:
        print("----------------------------------------")
        print("Ce contrat n'est pas signé. Impossible de créer un événement.")
