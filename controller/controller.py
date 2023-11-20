from views.view_collaborateur import ViewCollaborateur
from views.view_contrat import ViewContrat
from views.view_client import ViewClient
from views.view_evenement import ViewEvenement
from views.view_menu import ViewMenu
from models.collaborateur import Collaborateur
from models.role import Role
from models.client import Client
from models.contrat import Contrat
from models.evenement import Evenement
from dao.base import creer_database_tables, valider_session, supprimer_database_tables, valider_sessions_supprimer_objet
from typing import Union
from permissions.permissions_manager import Permissions
import datetime
import time



class Controller:

    @staticmethod
    def enregistrer_collaborateur(first_user_exists:bool) -> None:
        """Permet de creer instance d'un collaborateur"""
        prenom = ViewCollaborateur.entrer_prenom_collaborateur()
        nom = ViewCollaborateur.entrer_nom_collaborateur()
        email = ViewCollaborateur.entrer_email_collaborateur()
        telephone = ViewCollaborateur.entrer_telephone_collaborateur()
        mot_de_passe = ViewCollaborateur.entrer_mot_de_passe_collaborateur()
        roles = Role.lister_roles()
        roles_as_list_of_dict = [{role.id:role.role_name} for role in roles]

        if first_user_exists:
            role_id = ViewCollaborateur.choisir_role_collaborateur(roles_as_list_of_dict)
        else:
            roles = Role.lister_roles_par_nom("gestion")
            role_id = roles[0].id


        collaborateur = Collaborateur(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            mot_de_passe=mot_de_passe,
            role_id=role_id
            )

        

        collaborateur.hacher_mot_de_passe()

        ViewMenu.clear()
        ViewCollaborateur.confirmation_ajout_collaborateur(collaborateur)

        valider_session(collaborateur)


    @staticmethod
    def enregistrer_contrat() -> None:
        """Permet de creer instance d'un contrat"""
        montant_total = ViewContrat.entrer_montant_total()
        reste_a_payer = ViewContrat.entrer_reste_a_payer(montant_total)
        date_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        statut_signe = ViewContrat.choisir_statut()

        clients = Client.lister_clients_join_collaborateur()
        clients_as_list_of_dict = Client.clients_as_list_of_dict(clients)
        client_id = ViewContrat.choisir_client_id(clients_as_list_of_dict)

        # roles = Role.lister_roles_par_nom("commercial")
        # role = roles[0]
        # role_id = role.id

        # commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
        # commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
        # commercial_id = ViewContrat.choisir_collaborateur_id(commercial_as_list_of_dict)
        # collaborateur_id = commercial_id

        commercials = Collaborateur.selectionner_collaborateurs_par_client_id(client_id)
        commercial = commercials[0]

        contrat = Contrat(
            montant_total=montant_total,
            reste_a_payer=reste_a_payer,
            date_creation=date_creation,
            statut_signe=statut_signe,
            client_id=client_id,
            collaborateur_id=commercial.id
            )

        valider_session(contrat)


    @staticmethod
    def enregistrer_client(collaborateur_id:int) -> None:
        """Permet de creer instance d'un client"""
        prenom = ViewClient.entrer_prenom_client()
        nom = ViewClient.entrer_nom_client()
        email = ViewClient.entrer_email_client()
        telephone = ViewClient.entrer_telephone_client()
        entreprise = ViewClient.entrer_entreprise_client()
        date_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        collaborateur_id = collaborateur_id

        client = Client(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            entreprise=entreprise,
            date_creation=date_creation,
            collaborateur_id=collaborateur_id
        )

        valider_session(client)


    @staticmethod
    def enregistrer_evenement(contrat) -> None:
        """Permet de creer instance d'un evenement"""
        date_debut = ViewEvenement.entrer_date_debut_evenement()
        date_fin = ViewEvenement.entrer_date_fin_evenement()
        location_pays = ViewEvenement.entrer_pays_evenement()
        location_ville = ViewEvenement.entrer_ville_evenement()
        location_rue = ViewEvenement.entrer_rue_evenement()
        location_num_rue = ViewEvenement.entrer_numero_rue_evenement()
        location_cp = ViewEvenement.entrer_cp_evenement()
        attendees = ViewEvenement.entrer_attendees_evenement()
        notes = ViewEvenement.entrer_notes_evenement()

        evenement = Evenement(
            date_debut=date_debut,
            date_fin=date_fin,
            location_pays=location_pays,
            location_ville=location_ville,
            location_rue=location_rue,
            location_num_rue=location_num_rue,
            location_cp=location_cp,
            attendees=attendees,
            notes=notes,
            contrat_id=contrat.id
            )

        valider_session(evenement)


    @staticmethod
    def roles_existent_dans_db() -> bool:
        """Verification de l'existance des roles dans la base des donnees"""
        roles = []
        roles = Role.lister_roles()
        if roles:
            return True
        else:
            return False


    @staticmethod
    def initialiser_roles() -> None:
        """Ajout des roles par defaut dans la base des donnees"""
        roles = [role.value for role in Permissions.RolesEnum]
        Role.initialiser_roles(roles)


    @staticmethod
    def collaborateurs_existent_dans_db() -> bool:
        """Verification de l'existance des collaborateurs dans la base des donnees"""
        collaborateurs = []
        collaborateurs = Collaborateur.lister_collaborateurs()
        if collaborateurs:
            return True
        else:
            return False


    @staticmethod
    def authentication_user() -> Union[Collaborateur, None]:
        """Verification si l'utilisateur existe dans la base des donnees
        et que son mot de passe est correcte"""
        email = ViewCollaborateur.entrer_email_collaborateur()
        mot_de_pass = ViewCollaborateur.entrer_mot_de_passe_collaborateur()

        collaborateurs = Collaborateur.selectionner_collaborateurs_par_email(email)

        if not collaborateurs:
            ViewMenu.clear()
            ViewCollaborateur.refuser_authentification()
            return None
        
        collaborateur = collaborateurs[0]

        if collaborateur.verifier_mot_de_passe(mot_de_pass):
            return collaborateur
        else:
            ViewMenu.clear()
            ViewCollaborateur.refuser_authentification() 
            return None


    @staticmethod
    def check_authorization_permission(token:str, role:str, permission_demandee:str) -> bool:
        """Permet controler validite de token et permissions"""
        if not Collaborateur.verifier_token(token):
            ViewMenu.clear()
            ViewCollaborateur.refuser_token()
            return False

        if not Permissions.verification_persmissions_de_collaborateur(role, permission_demandee):
            ViewMenu.clear()
            ViewCollaborateur.refuser_permissions()
            return False
        
        return True


    @staticmethod
    def check_exclusive_permission(id_fkey:int, id:int) -> bool:
        if not id_fkey == id:
            ViewMenu.clear()
            ViewCollaborateur.refuser_permissions()
            return False
        
        return True
    

    @staticmethod
    def modifier_collaborateur(collaborateur:Collaborateur) -> None:
        """Modifie les informations d'un collaborateur"""
        
        role_list = Role.lister_roles_par_id(collaborateur.role_id)
        role = role_list[0]
        role_name = role.role_name

        attribut_dict = {
            "nom":collaborateur.nom,
            "prenom":collaborateur.prenom,
            "email":collaborateur.email,
            "telephone":collaborateur.telephone,
            "mot_de_passe":"*****",
            "role":role_name
            }
        
        for key, value in attribut_dict.items():
            if ViewCollaborateur.modifier_caracteristique(key,value):
                if key == "nom":
                    nom = ViewCollaborateur.entrer_nom_collaborateur()
                    collaborateur.nom = nom
                
                if key == "prenom":
                    prenom = ViewCollaborateur.entrer_prenom_collaborateur()
                    collaborateur.prenom = prenom

                if key == "email":
                    email = ViewCollaborateur.entrer_email_collaborateur()
                    collaborateur.email = email

                if key == "telephone":
                    telephone = ViewCollaborateur.entrer_telephone_collaborateur()
                    collaborateur.telephone = telephone
                    
                if key == "mot_de_passe":
                    mot_de_passe = ViewCollaborateur.entrer_mot_de_passe_collaborateur()
                    collaborateur.mot_de_passe = mot_de_passe
                    collaborateur.hacher_mot_de_passe()

                if key == "role":
                    roles = Role.lister_roles()
                    roles_as_list_of_dict = [{role.id:role.role_name} for role in roles]
                    role_id = ViewCollaborateur.choisir_role_collaborateur(roles_as_list_of_dict)
                    collaborateur.role_id = role_id


        valider_session(collaborateur)


    @staticmethod
    def modifier_contrat(contrat:Contrat) -> None:
        """Modifie les informations d'un contrat"""

        attribut_dict = {
            "montant_total":contrat.montant_total,
            "reste_a_payer":contrat.reste_a_payer,
            "statut_signe":contrat.statut_signe
            }

        for key, value in attribut_dict.items():
            if ViewContrat.modifier_caracteristique(key,value):
                if key == "montant_total":
                    montant_total = ViewContrat.entrer_montant_total()
                    contrat.montant_total = montant_total

                if key == "reste_a_payer":
                    reste_a_payer = ViewContrat.entrer_reste_a_payer(contrat.montant_total)
                    contrat.reste_a_payer = reste_a_payer

                if key == "statut_signe":
                    statut_signe = ViewContrat.choisir_statut()
                    contrat.statut_signe = statut_signe
    
        valider_session(contrat)


    @staticmethod
    def modifier_client(client:Client) -> None:
        """Modifie les informations d'un client"""

        attribut_dict = {
            "nom":client.nom,
            "prenom":client.prenom,
            "email":client.email,
            "telephone":client.telephone,
            "entreprise":client.entreprise
            }
        
        for key, value in attribut_dict.items():
            if ViewClient.modifier_caracteristique(key,value):
                if key == "nom":
                    nom = ViewClient.entrer_nom_client()
                    client.nom = nom
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                if key == "prenom":
                    prenom = ViewClient.entrer_prenom_client()
                    client.prenom = prenom
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                if key == "email":
                    email = ViewClient.entrer_email_client()
                    client.email = email
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                if key == "telephone":
                    telephone = ViewClient.entrer_telephone_client()
                    client.telephone = telephone
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                if key == "entreprise":
                    entreprise = ViewClient.entrer_entreprise_client()
                    client.entreprise = entreprise
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                # if key == "collaborateur_id":
                #     # Choisir parmis les commerciaux
                #     roles = Role.lister_roles_par_nom("commercial")
                #     role = roles[0]
                #     role_id = role.id

                #     commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
                #     commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
                #     commercial_id = ViewClient.choisir_collaborateur_id(commercial_as_list_of_dict)
                #     collaborateur_id = commercial_id

                #     client.collaborateur_id = collaborateur_id
                #     client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        valider_session(client)


    @staticmethod
    def modifier_evenement_gestion(evenement:Evenement) -> None:
        """Modifie les informations d'un evenement"""

        attribut_dict = {
            "date_debut":evenement.date_debut,
            "date_fin":evenement.date_fin,
            "location_pays":evenement.location_pays,
            "location_ville":evenement.location_ville,
            "location_rue":evenement.location_rue,
            "location_num_rue":evenement.location_num_rue,
            "location_cp":evenement.location_cp,
            "attendees":evenement.attendees,
            "notes":evenement.notes,
            "collaborateur_id":evenement.collaborateur_id,
            }
        

        
        for key, value in attribut_dict.items():
            if ViewEvenement.modifier_caracteristique(key,value):
                if key == "date_debut":
                    date_debut = ViewEvenement.entrer_date_debut_evenement()
                    evenement.date_debut = date_debut

                if key == "date_fin":
                    date_fin = ViewEvenement.entrer_date_fin_evenement()
                    evenement.date_fin = date_fin

                if key == "location_pays":
                    location_pays = ViewEvenement.entrer_pays_evenement()
                    evenement.location_pays = location_pays

                if key == "location_ville":
                    location_ville = ViewEvenement.entrer_ville_evenement()
                    evenement.location_ville = location_ville

                if key == "location_rue":
                    location_rue = ViewEvenement.entrer_rue_evenement()
                    evenement.location_rue = location_rue

                if key == "location_num_rue":
                    location_num_rue = ViewEvenement.entrer_numero_rue_evenement()
                    evenement.location_num_rue = location_num_rue

                if key == "location_cp":
                    location_cp = ViewEvenement.entrer_cp_evenement()
                    evenement.location_cp = location_cp

                if key == "attendees":
                    attendees = ViewEvenement.entrer_attendees_evenement()
                    evenement.attendees = attendees

                if key == "notes":
                    notes = ViewEvenement.entrer_notes_evenement()
                    evenement.notes = notes

                if key == "collaborateur_id":
                # Choisir parmis les supports
                    roles = Role.lister_roles_par_nom("support")
                    role = roles[0]
                    role_id = role.id

                    supports = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
                    supports_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(supports)
                    support_id = ViewEvenement.choisir_collaborateur_id(supports_as_list_of_dict)
                    collaborateur_id = support_id

                    evenement.collaborateur_id = collaborateur_id


        valider_session(evenement)


    @staticmethod
    def modifier_evenement_support(evenement:Evenement) -> None:
        """Modifie les informations d'un evenement"""

        attribut_dict = {
            "date_debut":evenement.date_debut,
            "date_fin":evenement.date_fin,
            "location_pays":evenement.location_pays,
            "location_ville":evenement.location_ville,
            "location_rue":evenement.location_rue,
            "location_num_rue":evenement.location_num_rue,
            "location_cp":evenement.location_cp,
            "attendees":evenement.attendees,
            "notes":evenement.notes,
            }
        

        
        for key, value in attribut_dict.items():
            if ViewEvenement.modifier_caracteristique(key,value):
                if key == "date_debut":
                    date_debut = ViewEvenement.entrer_date_debut_evenement()
                    evenement.date_debut = date_debut

                if key == "date_fin":
                    date_fin = ViewEvenement.entrer_date_fin_evenement()
                    evenement.date_fin = date_fin

                if key == "location_pays":
                    location_pays = ViewEvenement.entrer_pays_evenement()
                    evenement.location_pays = location_pays

                if key == "location_ville":
                    location_ville = ViewEvenement.entrer_ville_evenement()
                    evenement.location_ville = location_ville

                if key == "location_rue":
                    location_rue = ViewEvenement.entrer_rue_evenement()
                    evenement.location_rue = location_rue

                if key == "location_num_rue":
                    location_num_rue = ViewEvenement.entrer_numero_rue_evenement()
                    evenement.location_num_rue = location_num_rue

                if key == "location_cp":
                    location_cp = ViewEvenement.entrer_cp_evenement()
                    evenement.location_cp = location_cp

                if key == "attendees":
                    attendees = ViewEvenement.entrer_attendees_evenement()
                    evenement.attendees = attendees

                if key == "notes":
                    notes = ViewEvenement.entrer_notes_evenement()
                    evenement.notes = notes


        valider_session(evenement)



    @staticmethod
    def supprimer_obj(obj:Union[Collaborateur, Client, Contrat, Evenement]) -> None:
        """Supprime un objet"""
        valider_sessions_supprimer_objet(obj)


    @staticmethod
    def run() -> None:
        """Fonction qui lance l'application"""
        # supprimer_database_tables()
        # on initalise la base des donnees pour le premiere lancement de l'application
        creer_database_tables()

        # on initalise les roles pour le premiere lancement de l'application
        if not Controller.roles_existent_dans_db():
            Controller.initialiser_roles()

        # on initialise un utilisateur gestionnaire pour le premiere lancement de l'application
        collaborateur_existe_dans_db = Controller.collaborateurs_existent_dans_db()
        collaborateur = None
        ViewMenu.clear()
        if not collaborateur_existe_dans_db:
            ViewCollaborateur.initialisation_collaborateur()
            Controller.enregistrer_collaborateur(collaborateur_existe_dans_db)
            while collaborateur == None:
                ViewCollaborateur.demander_authentification()
                collaborateur = Controller.authentication_user()
        else:
            while collaborateur == None:
                ViewCollaborateur.demander_authentification()
                collaborateur = Controller.authentication_user()



        collaborateur_role_list = Role.lister_roles_par_id(collaborateur.role_id)
        collaborateur_role = collaborateur_role_list[0].role_name
        collaborateur_id = collaborateur.id

        token = collaborateur.generer_token()

        while True:
            ViewMenu.clear()
            choix_menu_principal = ViewMenu.afficher_menu_principal()
            
            if choix_menu_principal == "COLLABORATEURS":
                ViewMenu.clear()
                while True:
                    choix_menu_collaborateurs = ViewMenu.afficher_menu_model("collaborateur")
                    
                    if choix_menu_collaborateurs == "AFFICHER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "lecture_collaborateurs"):
                            while True:
                                collaborateurs = Collaborateur.lister_collaborateurs_join_roles()
                                ViewCollaborateur.afficher_collaborateurs(collaborateurs)
                                if ViewMenu.revenir_a_ecran_precedent() is True:
                                    ViewMenu.clear()
                                    break


                    if choix_menu_collaborateurs == "AJOUTER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "creer_collaborateur"):
                            while True:
                                collaborateur_existe_dans_db = Controller.collaborateurs_existent_dans_db()
                                Controller.enregistrer_collaborateur(collaborateur_existe_dans_db)
                                if ViewCollaborateur.redemander_ajouter_collaborateur() is False:
                                    ViewMenu.clear()
                                    break


                    if choix_menu_collaborateurs == "MODIFIER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "modifier_collaborateur"):
                            while True:
                                id = ViewCollaborateur.demander_id_du_collaborateur_a_modifier()
                                collaborateurs = Collaborateur.selectionner_collaborateurs_par_id(id)
                                collaborateur = collaborateurs[0]
                                Controller.modifier_collaborateur(collaborateur)
                                if ViewCollaborateur.demander_de_modifier_un_autre_collaborateur() is False:
                                    ViewMenu.clear()
                                    break
                                    


                    if choix_menu_collaborateurs == "SUPPRIMER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "supprimer_collaborateur"):
                            while True:
                                id = ViewCollaborateur.demander_id_du_collaborateur_a_supprimer()
                                collaborateurs = Collaborateur.selectionner_collaborateurs_par_id(id)
                                collaborateur = collaborateurs[0]
                                if ViewCollaborateur.demander_de_confirmer_suppression_collaborateur(collaborateur) is False:
                                    ViewMenu.clear()
                                    break
                                else:
                                    Controller.supprimer_obj(collaborateur)
                                    ViewMenu.clear()
                                    break

                    if choix_menu_collaborateurs == "REVENIR":
                        ViewMenu.clear()
                        break

                    if choix_menu_collaborateurs == "QUITTER":
                        exit()


            if choix_menu_principal == "CLIENTS":
                ViewMenu.clear()
                while True:
                    choix_menu_clients = ViewMenu.afficher_menu_model("client")
                    
                    if choix_menu_clients == "AFFICHER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "lecture_clients"):
                            while True:
                                clients = Client.lister_clients_join_collaborateur()
                                ViewClient.afficher_clients(clients)
                                if ViewMenu.revenir_a_ecran_precedent() is True:
                                    ViewMenu.clear()
                                    break
            
                    if choix_menu_clients == "AJOUTER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "creer_client"):
                            while True:
                                Controller.enregistrer_client(collaborateur_id)
                                if ViewClient.redemander_ajouter_client() is False:
                                    ViewMenu.clear()
                                    break

                    if choix_menu_clients == "MODIFIER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "modifier_client"):
                            while True:
                                id = ViewClient.demander_id_du_client_a_modifier()
                                clients = Client.selectionner_client_par_id(id)
                                client = clients[0]

                                if Controller.check_exclusive_permission(
                                    id_fkey=client.collaborateur_id,
                                    id=collaborateur_id
                                    ) is False:
                                    break
                                
                                Controller.modifier_client(client)
                                if ViewClient.demander_de_modifier_un_autre_client() is False:
                                    ViewMenu.clear()
                                    break


                    if choix_menu_clients == "SUPPRIMER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "supprimer_client"):
                            while True:
                                id = ViewClient.demander_id_du_client_a_supprimer()
                                clients = Client.selectionner_client_par_id(id)
                                client = clients[0]

                                if Controller.check_exclusive_permission(
                                    id_fkey=client.collaborateur_id,
                                    id=collaborateur_id
                                    ) is False:
                                    break

                                if ViewClient.demander_de_confirmer_suppression_client(client) is False:
                                    ViewMenu.clear()
                                    break
                                else:
                                    Controller.supprimer_obj(client)
                                    ViewMenu.clear()
                                    break

                    
                    if choix_menu_clients == "REVENIR":
                        ViewMenu.clear()
                        break

                    if choix_menu_clients == "QUITTER":
                        exit()


            if choix_menu_principal == "CONTRATS":
                ViewMenu.clear()
                while True:
                    choix_menu_contrat = ViewMenu.afficher_menu_model("contrat")
                    
                    if choix_menu_contrat == "AFFICHER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "lecture_contrats"):
                            while True:
                                if collaborateur_role == "commercial":
                                   
                                    choix_filtre_contrat = ViewMenu.afficher_menu_filtre_contrat()
                                    
                                    if choix_filtre_contrat == "TOUS":
                                        while True:
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client()

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break
                                    
                                    if choix_filtre_contrat == "SIGNE":
                                        while True:
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client_signature(True)

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_contrat == "NON_SIGNE":
                                        while True:
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client_signature(False)

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break
                                    
                                    if choix_filtre_contrat == "PAYE":
                                        while True:
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client_paye()

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_contrat == "NON_PAYE":
                                        while True:
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client_non_paye()

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_contrat == "PAR_CLIENT":
                                        while True:
                                            client_id = ViewClient.demander_id_du_client_a_filtrer()
                                            contrats = Contrat.lister_contrats_join_collaborateur_join_client_par_client(client_id)

                                            ViewContrat.afficher_contrats(contrats)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break


                                    if choix_filtre_contrat == "REVENIR":
                                        ViewMenu.clear()
                                        break

                                    if choix_filtre_contrat == "QUITTER":
                                        exit()

                                else:
                                    contrats = Contrat.lister_contrats_join_collaborateur_join_client()

                                    ViewContrat.afficher_contrats(contrats)
                                    if ViewMenu.revenir_a_ecran_precedent() is True:
                                        ViewMenu.clear()
                                        break

                    
                    if choix_menu_contrat == "AJOUTER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "creer_contrat"):
                            while True:
                                Controller.enregistrer_contrat()
                                if ViewContrat.redemander_ajouter_contrat() is False:
                                    ViewMenu.clear()
                                    break

                    if choix_menu_contrat == "MODIFIER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "modifier_contrat"):
                            while True:
                                id = ViewContrat.demander_id_du_contrat_a_modifier()
                                contrats = Contrat.lister_contrats_par_id(id)
                                if not contrats:
                                    ViewContrat.contrat_avec_id_nexiste_pas(id)
                                    break
                                contrat = contrats[0]

                                if collaborateur_role == "commercial":
                                    if Controller.check_exclusive_permission(
                                        id_fkey=contrat.collaborateur_id,
                                        id=collaborateur_id
                                        ) is False:
                                        break

                                Controller.modifier_contrat(contrat)
                                if ViewContrat.redemander_modifier_un_autre_contrat() is False:
                                    ViewMenu.clear()
                                    break
                
                    if choix_menu_contrat == "SUPPRIMER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "supprimer_contrat"):
                            while True:
                                id = ViewContrat.demander_id_du_contrat_a_supprimer()
                                contrats = Contrat.lister_contrats_par_id(id)
                                if not contrats:
                                    ViewContrat.contrat_avec_id_nexiste_pas(id)
                                    break
                                contrat = contrats[0]

                                if ViewContrat.demander_de_confirmer_suppression_contrat(contrat) is False:
                                    ViewMenu.clear()
                                    break
                                else:
                                    Controller.supprimer_obj(contrat)
                                    ViewMenu.clear()
                                    break


                    if choix_menu_contrat == "REVENIR":
                        ViewMenu.clear()
                        break

                    if choix_menu_contrat == "QUITTER":
                        exit()


            if choix_menu_principal == "EVENEMENTS":
                ViewMenu.clear()
                while True:
                    choix_menu_evenement = ViewMenu.afficher_menu_model("evenement")
                    
                    if choix_menu_evenement == "AFFICHER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "lecture_evenements"):
                            while True:
                                if collaborateur_role == "support":
                                    choix_filtre_evenement = ViewMenu.afficher_menu_filtre_evenement_support()
                                    
                                    if choix_filtre_evenement == "TOUS":
                                        while True:
                                            evenements = Evenement.lister_evenements_join_contrat_collaborateurs_client()

                                            ViewEvenement.afficher_evenements(evenements)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break
                                    
                                    if choix_filtre_evenement == "MES_EVENEMENTS":
                                        while True:
                                            evenements = Evenement.lister_evenements_par_collaborateur(collaborateur_id)

                                            ViewEvenement.afficher_evenements(evenements)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_evenement == "REVENIR":
                                        ViewMenu.clear()
                                        break

                                    if choix_filtre_evenement == "QUITTER":
                                        exit()

                                elif collaborateur_role == "gestion":
                                    choix_filtre_evenement = ViewMenu.afficher_menu_filtre_evenement_gestion()
                                    
                                    if choix_filtre_evenement == "TOUS":
                                        while True:
                                            evenements = Evenement.lister_evenements_join_contrat_collaborateurs_client()

                                            ViewEvenement.afficher_evenements(evenements)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_evenement == "SANS_SUPPORT":
                                        while True:
                                            evenements = Evenement.lister_evenements_sans_collaborateur()

                                            ViewEvenement.afficher_evenements(evenements)
                                            if ViewMenu.revenir_a_ecran_precedent() is True:
                                                ViewMenu.clear()
                                                break

                                    if choix_filtre_evenement == "REVENIR":
                                        ViewMenu.clear()
                                        break

                                    if choix_filtre_evenement == "QUITTER":
                                        exit()

                                else:
                                    evenements = Evenement.lister_evenements_join_contrat_collaborateurs_client()
                                    ViewEvenement.afficher_evenements(evenements)
                                    if ViewMenu.revenir_a_ecran_precedent() is True:
                                        ViewMenu.clear()
                                        break

                    if choix_menu_evenement == "AJOUTER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "creer_evenement"):
                            while True:
                                id = ViewContrat.demander_id_du_contrat_pour_evenement()
                                contrats = Contrat.lister_contrats_par_id(id)
                                if not contrats:
                                    ViewContrat.contrat_avec_id_nexiste_pas(id)
                                    break
                                contrat = contrats[0]

                                if collaborateur_role == "commercial":
                                    if Controller.check_exclusive_permission(
                                        id_fkey=contrat.collaborateur_id,
                                        id=collaborateur_id
                                        ) is False:
                                        break

                                if contrat.statut_signe is False:
                                    ViewContrat.contrat_avec_id_nest_pas_signe()
                                    break


                                Controller.enregistrer_evenement(contrat)
                                if ViewEvenement.redemander_ajouter_evenement() is False:
                                    ViewMenu.clear()
                                    break

                    if choix_menu_evenement == "MODIFIER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "modifier_evenement"):
                            while True:
                                id = ViewEvenement.demander_id_de_evenement_a_modifier()
                                evenements = Evenement.lister_evenements_par_id(id)

                                if not evenements:
                                    ViewEvenement.evenement_avec_id_nexiste_pas(id)
                                    break
                                evenement = evenements[0]

                                if collaborateur_role == "support":
                                    if Controller.check_exclusive_permission(
                                        id_fkey=evenement.collaborateur_id,
                                        id=collaborateur_id
                                        ) is False:
                                        break
                                
                                if collaborateur_role == "gestion":
                                    Controller.modifier_evenement_gestion(evenement)

                                if collaborateur_role == "support":
                                    Controller.modifier_evenement_support(evenement)
                                
                                if ViewEvenement.redemander_modifier_un_autre_evenement() is False:
                                    ViewMenu.clear()
                                    break

                    if choix_menu_evenement == "SUPPRIMER":
                        ViewMenu.clear()
                        if Controller.check_authorization_permission(token, collaborateur_role, "supprimer_evenement"):
                            while True:
                                id = ViewEvenement.demander_id_evenement_a_supprimer()
                                evenements = Evenement.lister_evenements_par_id(id)
                                if not evenements:
                                    ViewEvenement.evenement_avec_id_nexiste_pas(id)
                                    break
                                evenement = evenements[0]

                                if ViewEvenement.demander_de_confirmer_suppression_evenement(contrat) is False:
                                    ViewMenu.clear()
                                    break
                                else:
                                    Controller.supprimer_obj(contrat)
                                    ViewMenu.clear()
                                    break

                    if choix_menu_evenement == "REVENIR":
                        ViewMenu.clear()
                        break

                    if choix_menu_evenement == "QUITTER":
                        exit()

            if choix_menu_principal == "QUITTER":
                exit()
