from dao.base import Session, creer_database_tables, supprimer_database_tables
from models.client import Client
from models.collaborateur import Collaborateur
from models.contrat import Contrat
from models.evenement import Evenement
from models.role import Role
from controller.controller import Controller


# supprimer_database_tables()
creer_database_tables()

if Controller.roles_existe_dans_db():
    pass
else:
    Controller.ajouter_roles()

Controller.authentication_user()


# Controller.enregistrer_collaborateur()
