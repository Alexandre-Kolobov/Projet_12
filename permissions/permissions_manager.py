from views.view_collaborateur import ViewCollaborateur
from models.collaborateur import Collaborateur
from models.role import Role
from dao.base import ouvrir_session, add_session, commit_session, close_session
from typing import Union
from enum import Enum

class Permissions:
    class RolesEnum(Enum):
        GESTION = "gestion"
        COMMERCIAL = "commercial"
        SUPPORT = "support"


    class PermissionsEnum(Enum):
        LECTURE_COLLABORATEURS = "lecture_collaborateurs"
        CREER_COLLABORATEURS = "creer_collaborateur"
        MODIFIER_COLLABORATEURS = "modifier_collaborateur"
        SUPPRIMER_COLLABORATEURS = "supprimer_collaborateur"

        LECTURE_CLIENTS = "lecture_clients"
        CREER_CLIENTS = "creer_client"
        MODIFIER_CLIENTS = "modifier_client"
        SUPPRIMER_CLIENTS = "supprimer_client"

        LECTURE_CONTRATS = "lecture_contrats"
        CREER_CONTRATS = "creer_contrat"
        MODIFIER_CONTRATS = "modifier_contrat"
        SUPPRIMER_CONTRATS = "supprimer_contrat"

    @staticmethod
    def verification_persmissions_de_collaborateur(
        collaborateur_role:str,
        permission_demandee:PermissionsEnum
        ) -> bool:

        """Verification de combinaison de role et de permissions"""
        RolesEnum = Permissions.RolesEnum
        PermissionsEnum = Permissions.PermissionsEnum
        # role_id = collaborateur.role_id
        # role = Role.lister_roles_par_id(role_id)

        # Permissions gestionnaire - collaborateur:
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.LECTURE_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEURS.value:
            return True
        

        # Permissions commercial - collaborateur:
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEURS.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEURS.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEURS.value:
            return False
        

        # Permissions support - collaborateur:
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.LECTURE_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEURS.value:
            return False
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEURS.value:
            return False
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEURS.value:
            return False
        

        # Permissions gestionnaire - client:
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.LECTURE_CLIENTS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.CREER_CLIENTS.value:
            return False
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.MODIFIER_CLIENTS.value:
            return False
          
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.SUPPRIMER_CLIENTS.value:
            return False
        

        # Permissions commercial - client:
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_CLIENTS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.CREER_CLIENTS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.MODIFIER_CLIENTS.value:
            return True
          
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.SUPPRIMER_CLIENTS.value:
            return True
        
    
        # Permissions support - client:
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.LECTURE_CLIENTS.value:
            return True
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.CREER_CLIENTS.value:
            return False
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.MODIFIER_CLIENTS.value:
            return False
          
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.SUPPRIMER_CLIENTS.value:
            return False



        # Permissions gestionnaire - contrat:
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.CREER_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.MODIFIER_CONTRATS.value:
            return True
          
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.SUPPRIMER_CONTRATS.value:
            return True
        

        # Permissions commercial - contrat:
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.CREER_CONTRATS.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.MODIFIER_CONTRATS.value:
            return False
          
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.SUPPRIMER_CONTRATS.value:
            return False


        # Permissions support - contrat:
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.CREER_CONTRATS.value:
            return False
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.MODIFIER_CONTRATS.value:
            return False
          
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.SUPPRIMER_CONTRATS.value:
            return False
        



        
        return False