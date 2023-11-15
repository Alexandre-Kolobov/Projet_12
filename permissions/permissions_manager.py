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
        CREER_COLLABORATEUR = "creer_collaborateur"
        MODIFIER_COLLABORATEUR = "modifier_collaborateur"
        SUPPRIMER_COLLABORATEUR = "supprimer_collaborateur"
        LECTURE_CONTRATS = "lecture_contrats"

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
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEUR.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEUR.value:
            return True
        
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEUR.value:
            return True
        

        # Permissions commercial - collaborateur:
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEUR.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEUR.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEUR.value:
            return False
        

        # Permissions support - collaborateur:
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_COLLABORATEURS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.CREER_COLLABORATEUR.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.MODIFIER_COLLABORATEUR.value:
            return False
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.SUPPRIMER_COLLABORATEUR.value:
            return False
        
        

        
        # Permissions contrat
        if collaborateur_role == RolesEnum.GESTION.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.COMMERCIAL.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True
        
        if collaborateur_role == RolesEnum.SUPPORT.value and permission_demandee == PermissionsEnum.LECTURE_CONTRATS.value:
            return True

        
        return False