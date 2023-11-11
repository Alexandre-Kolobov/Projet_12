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
from dao.base import creer_database_tables, valider_session, supprimer_database_tables
from typing import Union
from permissions.permissions_manager import Permissions
import datetime



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

        valider_session(collaborateur)

    @staticmethod
    def enregistrer_contrat() -> None:
        """Permet de creer instance d'un contrat"""
        montant_total = ViewContrat.entrer_montant_total()
        reste_a_payer = ViewContrat.entrer_reste_a_payer()
        date_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        statut_signe = ViewContrat.choisir_statut()

        clients = Client.clients_as_list_of_dict()
        clients_as_list_of_dict = Client.clients_as_list_of_dict(clients)
        client_id = ViewContrat.choisir_client_id(clients_as_list_of_dict)

        roles = Role.lister_roles_par_nom("commercial")
        role = roles[0]
        role_id = role.id

        commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
        commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
        commercial_id = ViewContrat.choisir_collaborateur_id(commercial_as_list_of_dict)
        collaborateur_id = commercial_id

        contrat = Contrat(
            montant_total=montant_total,
            reste_a_payer=reste_a_payer,
            date_creation=date_creation,
            statut_signe=statut_signe,
            client_id=client_id,
            collaborateur_id=collaborateur_id
            )

        valider_session(contrat)


    @staticmethod
    def enregistrer_client() -> None:
        """Permet de creer instance d'un client"""
        nom = ViewClient.entrer_nom_client()
        prenom = ViewClient.entrer_prenom_client()
        email = ViewClient.entrer_email_client()
        telephone = ViewClient.entrer_telephone_client()
        entreprise = ViewClient.entrer_entreprise_client()
        date_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        roles = Role.lister_roles_par_nom("commercial")
        role = roles[0]
        role_id = role.id

        commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
        commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
        commercial_id = ViewClient.choisir_collaborateur_id(commercial_as_list_of_dict)
        collaborateur_id = commercial_id


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
    def enregistrer_evenement() -> None:
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
        contrat_id = ViewEvenement.entrer_contrat_id_evenement()

        roles = Role.lister_roles_par_nom("support")
        role = roles[0]
        role_id = role.id

        support = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
        support_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(support)
        support_id = ViewContrat.choisir_collaborateur_id(support_as_list_of_dict)
        collaborateur_id = support_id

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
            contrat_id=contrat_id,
            collaborateur_id=collaborateur_id
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
            ViewCollaborateur.refuser_authentification()
            return None
        
        collaborateur = collaborateurs[0]

        if collaborateur.verifier_mot_de_passe(mot_de_pass):
            return collaborateur
        else:
            ViewCollaborateur.refuser_authentification() 
            return None


    @staticmethod
    def check_authorization_permission(token:str, role:str, permission_demandee:str) -> bool:
        """Permet controler validite de token et permissions"""
        if not Collaborateur.verifier_token:
            ViewCollaborateur.refuser_token()
            return False

        if not Permissions.verification_persmissions_de_collaborateur(role, permission_demandee):
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
            "statut_signe":contrat.statut_signe,
            "client_id":contrat.client_id,
            "collaborateur_id":contrat.collaborateur_id
            }

        for key, value in attribut_dict.items():
            if ViewContrat.modifier_caracteristique(key,value):
                if key == "montant_total":
                    montant_total = ViewContrat.entrer_montant_total()
                    contrat.montant_total = montant_total

                if key == "reste_a_payer":
                    reste_a_payer = ViewContrat.entrer_reste_a_payer()
                    contrat.reste_a_payer = reste_a_payer

                if key == "statut_signe":
                    statut_signe = ViewContrat.choisir_statut()
                    contrat.statut_signe = statut_signe
 
                if key == "client_id":
                    clients = Client.clients_as_list_of_dict()
                    clients_as_list_of_dict = Client.clients_as_list_of_dict(clients)
                    client_id = ViewContrat.choisir_client_id(clients_as_list_of_dict)
                    contrat.client_id = client_id

                if key == "collaborateur_id":
                    # Choisir parmis les commerciaux
                    roles = Role.lister_roles_par_nom("commercial")
                    role = roles[0]
                    role_id = role.id

                    commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
                    commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
                    commercial_id = ViewContrat.choisir_collaborateur_id(commercial_as_list_of_dict)
                    collaborateur_id = commercial_id

                    contrat.collaborateur_id = collaborateur_id
    
        valider_session(contrat)


    @staticmethod
    def modifier_client(client:Client) -> None:
        """Modifie les informations d'un client"""

        attribut_dict = {
            "nom":client.nom,
            "prenom":client.prenom,
            "email":client.email,
            "telephone":client.telephone,
            "entreprise":client.entreprise,
            "collaborateur_id":client.collaborateur_id
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

                if key == "collaborateur_id":
                    # Choisir parmis les commerciaux
                    roles = Role.lister_roles_par_nom("commercial")
                    role = roles[0]
                    role_id = role.id

                    commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
                    commercial_as_list_of_dict = Collaborateur.collaborateurs_as_list_of_dict(commercials)
                    commercial_id = ViewClient.choisir_collaborateur_id(commercial_as_list_of_dict)
                    collaborateur_id = commercial_id

                    client.collaborateur_id = collaborateur_id
                    client.date_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        valider_session(client)


    @staticmethod
    def modifier_evenement(evenement:Evenement) -> None:
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
            "contrat_id":evenement.contrat_id,
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

                if key == "contrat_id":
                    contrat_id = ViewEvenement.entrer_contrat_id_evenement()
                    evenement.contrat_id = contrat_id

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
        if not collaborateur_existe_dans_db:
            ViewCollaborateur.initialisation_collaborateur()
            Controller.enregistrer_collaborateur(collaborateur_existe_dans_db)
            while collaborateur == None:
                collaborateur = Controller.authentication_user()
        else:
            while collaborateur == None:
                collaborateur = Controller.authentication_user()



        collaborateur_role_list = Role.lister_roles_par_id(collaborateur.role_id)
        collaborateur_role = collaborateur_role_list[0].role_name

        token = collaborateur.generer_token()


        choix = ViewMenu.afficher_menu_principal()
        if choix == "Consulter":
            list_collaborateur = Collaborateur.lister_collaborateurs()
            ViewMenu.afficher_collaborateurs(list_collaborateur)

            

        # # Controller.enregistrer_contrat()
        # # contrats = Contrat.lister_contrats()
        # # Controller.modifier_contrat(contrats[1])
        # Controller.enregistrer_client()
