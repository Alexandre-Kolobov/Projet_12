from views.view_collaborateur import ViewCollaborateur
from models.collaborateur import Collaborateur
from models.role import Role
from typing import List
from dao.base import creer_database_tables, ouvrir_session, add_session, commit_session, close_session


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
    def ajouter_roles() -> None:
        """Ajout des roles par defaut dans la base des donnees"""
        roles = ["gestion", "commercial", "support"]

        session = ouvrir_session()
        for r in roles:
            role = Role(role_name=r)
        
            add_session(session, role)

        commit_session(session)
        close_session(session)


    @staticmethod
    def authentication_user() -> bool:
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
            return True
        else:
            ViewCollaborateur.refuser_authentification() 
            return False

