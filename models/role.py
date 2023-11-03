from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dao.base import Base
from dao.role_queries import RoleQueries
from typing import List


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String(50), nullable=False)

    collaborateurs = relationship("Collaborateur", back_populates="role")


    def __repr__(self):
        return (f"id{self.id} {self.role_name}")
    
    @staticmethod
    def lister_roles() -> List["Role"]:
        """Renvoi la liste de tous les roles"""
        return(RoleQueries.lister_roles_dao(Role))
    
    @staticmethod
    def initialiser_roles(roles: list) -> None:
        """Ajout des roles dans la base des donnees"""
        for r in roles:
            role = Role(role_name=r)
            RoleQueries.ajouter_role_dao(role)

    @staticmethod
    def lister_roles_par_id(role_id) -> List["Role"]:
        """Renvoi la liste de tous les roles en fonction de leur id"""
        return(RoleQueries.lister_roles_par_id_dao(Role, role_id))
    

    @staticmethod
    def lister_roles_par_nom(role_name) -> List["Role"]:
        """Renvoi la liste de tous les roles en fonction de leur nom"""
        return(RoleQueries.lister_roles_par_name_dao(Role, role_name))
