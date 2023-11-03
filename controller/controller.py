from views.view_collaborateur import ViewCollaborateur
from views.view_contrat import ViewContrat
from models.collaborateur import Collaborateur
from models.role import Role
from models.client import Client
from models.contrat import Contrat
from models.evenement import Evenement
from dao.base import creer_database_tables, valider_session
from typing import Union
from permissions.permissions_manager import Permissions
import datetime


class Controller:

    @staticmethod
    def enregistrer_collaborateur() -> None:
        """Permet de creer instance d'un collaborateur"""
        prenom = ViewCollaborateur.entrer_prenom_collaborateur()
        nom = ViewCollaborateur.entrer_nom_collaborateur()
        email = ViewCollaborateur.entrer_email_collaborateur()
        telephone = ViewCollaborateur.entrer_telephone_collaborateur()
        mot_de_passe = ViewCollaborateur.entrer_mot_de_passe_collaborateur()

        roles = Role.lister_roles()
        roles_as_list_of_dict = [{role.id:role.role_name} for role in roles]
        role_id = ViewCollaborateur.choisir_role_collaborateur(roles_as_list_of_dict)

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
        date_creation = datetime.datetime.now()
        statut_signe = ViewContrat.choisir_statut()

        clients = Client.lister_clients()
        clients_as_list_of_dict = [{client.id:f"{client.nom} {client.prenom} - {client.entreprise}"} for client in clients]
        client_id = ViewContrat.choisir_client_id(clients_as_list_of_dict)

        roles = Role.lister_roles_par_nom("commercial")
        role = roles[0]
        role_id = role.id

        commercials = Collaborateur.selectionner_collaborateurs_par_role_id(role_id)
        commercial_as_list_of_dict = [{commercial.id:f"{commercial.nom} {commercial.prenom}"} for commercial in commercials]
        commercial_id = ViewContrat.choisir_client_id(commercial_as_list_of_dict)

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
    def roles_existe_dans_db() -> bool:
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
        roles = [role.value for role in Controller.RolesEnum]
        Role.initialiser_roles(roles)


    @staticmethod
    def authentication_user() -> Union[Collaborateur, None]:
        """Verification si l'utilisateur existe dans la base des donnees
        et que son mot de passe est correcte"""
        email = ViewCollaborateur.entrer_email_collaborateur()
        mot_de_pass = ViewCollaborateur.entrer_mot_de_passe_collaborateur()

        collaborateurs = Collaborateur.selectionner_collaborateurs_par_email(email)

        if not collaborateurs:
            ViewCollaborateur.refuser_authentification()
            return False
        
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
    def run() -> None:
        """Fonction qui lance l'application"""

        creer_database_tables()
        if not Controller.roles_existe_dans_db():
            Controller.initialiser_roles()

        collaborateur = Controller.authentication_user()
        collaborateur_role_list = Role.lister_roles_par_id(collaborateur.role_id)
        collaborateur_role = collaborateur_role_list[0].role_name
        token = collaborateur.generer_token()

        Controller.enregistrer_contrat()