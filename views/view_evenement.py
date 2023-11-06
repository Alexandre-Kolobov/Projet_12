import datetime
class ViewEvenement():

    @staticmethod
    def entrer_date_debut_evenement() -> datetime.date:
            while True:
                print("----------------------------------------")
                try:
                    date = input("Entrer la date de debut de l'evenement DD/MM/YYYY hh:mm:ss : ").strip()
                    date_format = "%d/%m/%Y %H:%M:%S"
                    if not datetime.strptime(date, date_format):
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
                    if not datetime.strptime(date, date_format):
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
        while True:
            print("----------------------------------------")
            try:
                note = input("Entrer une note pour l'evenement: ").strip()
                if not note == "":
                    raise ValueError("Une note de l'evenement ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

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
            print("Choissisez le support à assigner pour cet evenement:")
            for collaborateur in collaborateur_as_list_of_dict:
                for key, value in collaborateur.items():
                    print(f"{key} - {value}")
            
            
            try:
                choix_collaborateur = input("Entrer le numero du support: ").strip()
                if not choix_collaborateur.isnumeric() or choix_collaborateur == "":
                    raise ValueError("Merci de choisir parmis les collaborateurs proposés")
                
                choix_collaborateur = int(choix_collaborateur)
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