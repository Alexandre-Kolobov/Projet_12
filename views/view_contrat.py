class ViewContrat():
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
    
    def entrer_reste_a_payer() -> int:
        while True:
            print("----------------------------------------")
            try:
                reste = input("Entrer le reste a payer du contrat: ").strip()
                if not reste.isnumeric() or reste == "":
                    raise ValueError("Le reste a payer du contrat doit être numerique et ne pas être vide")
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
    def choisir_client_id(clients_as_list_of_dict:list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le client à assigner pour ce contrat:")
            for client in clients_as_list_of_dict:
                for key, value in client.items():
                    print(f"{key} - {value}")
            
            
            try:
                choix_client = input("Entrer le numero du client: ").strip()
                if not choix_client.isnumeric() or choix_client == "":
                    raise ValueError("Merci de choisir parmis les roles proposés")
                
                choix_client = int(choix_client)
                break
            except ValueError as exc:
                print("Erreur: " + str(exc))

        return choix_client
    

    @staticmethod
    def choisir_collaborateur_id(collaborateur_as_list_of_dict:list[dict]) -> int:
        while True:
            print("----------------------------------------")
            print("Choissisez le collaborateur à assigner pour ce contrat:")
            for collaborateur in collaborateur_as_list_of_dict:
                for key, value in collaborateur.items():
                    print(f"{key} - {value}")
            
            
            try:
                choix_collaborateur = input("Entrer le numero du collaborateur: ").strip()
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