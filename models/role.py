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