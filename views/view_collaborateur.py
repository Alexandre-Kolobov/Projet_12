class ViewCollaborateur():
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
                mot_de_passe = input("Entrer le mot de passe du collaborateur: ").strip()
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
    def refuser_authentification() -> str:
        print("Les informations d'identification ne sont pas correctes")