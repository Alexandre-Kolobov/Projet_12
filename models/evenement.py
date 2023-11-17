from sqlalchemy import ForeignKey, DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dao.base import Base
from datetime import datetime
from dao.evenement_queries import EvenementQueries
from typing import List


class Evenement(Base):
    __tablename__ = "evenement"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_debut: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_fin: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location_pays: Mapped[str] = mapped_column(String(50), nullable=False)
    location_ville: Mapped[str] = mapped_column(String(50), nullable=False)
    location_rue: Mapped[str] = mapped_column(String(100), nullable=False)
    location_num_rue: Mapped[int] = mapped_column(Integer, nullable=False)
    location_cp: Mapped[int] = mapped_column(Integer, nullable=False)
    attendees: Mapped[int] = mapped_column(Integer, nullable=False)
    notes: Mapped[str] = mapped_column(String(1000), nullable=False)
    contrat_id: Mapped[int] = mapped_column(ForeignKey("contrat.id"), nullable=False)
    collaborateur_id: Mapped[int] = mapped_column(ForeignKey("collaborateur.id"), nullable=True)

    contrat = relationship("Contrat", uselist=False, back_populates="evenement")
    collaborateur = relationship("Collaborateur", back_populates="evenements")

    @staticmethod
    def lister_evenements() -> List["Evenement"]:
        """Renvoi la liste des evenements"""
        return(EvenementQueries.lister_evenements_dao(Evenement))
    
    @staticmethod
    def lister_evenements_join_contrat_collaborateurs_client() -> List["Evenement"]:
        """Renvoi la liste des evenements"""
        return(EvenementQueries.lister_evenements_join_contrat_collaborateurs_client_dao(Evenement))
    
    @staticmethod
    def lister_evenements_par_collaborateur(id) -> List["Evenement"]:
        """Renvoi la liste des evenements"""
        return(EvenementQueries.lister_evenements_par_collaborateur_dao(Evenement, id))
    
    @staticmethod
    def lister_evenements_par_id(id) -> List["Evenement"]:
        """Renvoi la liste des evenements"""
        return(EvenementQueries.lister_evenements_par_id_dao(Evenement, id))
    

    @staticmethod
    def lister_evenements_sans_collaborateur() -> List["Evenement"]:
        """Renvoi la liste des evenements"""
        return(EvenementQueries.lister_evenements_sans_collaborateur_dao(Evenement, id))