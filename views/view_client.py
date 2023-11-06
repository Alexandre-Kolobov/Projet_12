class ViewClient():

    @staticmethod
    def entrer_prenom_client() -> str:
            while True:
                print("----------------------------------------")
                try:
                    prenom = input("Entrer le prénom du client: ").strip()
                    if not prenom.isalpha() or prenom == "":
                        raise ValueError("Le prénom du client doit contenir que des lettres et ne pas être vide")
                    break
                except ValueError as exc:
                    print("Erreur: " + str(exc))

            return prenom


    @staticmethod
    def entrer_nom_client() -> str:
        while True:
            print("----------------------------------------")
            try:
                nom = input("Entrer le nom du client: ").strip()
                if not nom.isalpha() or nom == "":
                    raise ValueError("Le nom du client doit contenir que des lettres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return nom


    @staticmethod
    def entrer_email_client() -> str:
        while True:
            print("----------------------------------------")
            try:
                email = input("Entrer l'email du client: ").strip()
                if email == "":
                    raise ValueError("L'email du client ne doit pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return email


    @staticmethod
    def entrer_telephone_client() -> int:
        while True:
            print("----------------------------------------")
            try:
                telephone = input("Entrer le numero telephone du client: ").strip()
                if not telephone.isnumeric() or telephone == "":
                    raise ValueError("Le numero telephone doit contenir que des chiffres et ne pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return telephone


    @staticmethod
    def entrer_entreprise_client() -> str:
        while True:
            print("----------------------------------------")
            try:
                entreprise = input("Entrer l'entreprise du collaborateur: ").strip()
                if entreprise == "":
                    raise ValueError("L'entreprise du collaborateur ne doit pas être vide")
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return entreprise


    @staticmethod
    def choisir_collaborateur_id(collaborateur_as_list_of_dict:list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le commercial à assigner pour ce client:")
            for collaborateur in collaborateur_as_list_of_dict:
                for key, value in collaborateur.items():
                    print(f"{key} - {value}")
            
            
            try:
                choix_collaborateur = input("Entrer le numero du commercial: ").strip()
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