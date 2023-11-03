from views.view_collaborateur import ViewCollaborateur
from models.collaborateur import Collaborateur
from models.role import Role
from models.client import Client
from models.contrat import Contrat
from models.evenement import Evenement
from dao.base import ouvrir_session, add_session, commit_session, close_session, creer_database_tables
from typing import Union
from permissions.permissions_manager import Permissions


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

        session = ouvrir_session()
        add_session(session, collaborateur)
        commit_session(session)
        close_session(session)


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
    def run() -> None:
        """Fonction qui lance l'application"""

        creer_database_tables()
        if not Controller.roles_existe_dans_db():
            Controller.initialiser_roles()

        collaborateur = Controller.authentication_user()
        collaborateur_role_list = Role.lister_roles_par_id(collaborateur.role_id)
        collaborateur_role = collaborateur_role_list[0].role_name
        token = collaborateur.generer_token()

        if Controller.check_authorization_permission(token, collaborateur_role, "creer_collaborateur"):
            Controller.enregistrer_collaborateur()



    