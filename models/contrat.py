from sqlalchemy import ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dao.base import Base
from datetime import datetime
from dao.contrat_queries import ContratQueries
from typing import List


class Contrat(Base):
    __tablename__ = "contrat"

    id: Mapped[int] = mapped_column(primary_key=True)
    montant_total: Mapped[float] = mapped_column(Float, nullable=False)
    reste_a_payer: Mapped[float] = mapped_column(Float, nullable=False)
    date_creation: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    statut_signe: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    collaborateur_id: Mapped[int] = mapped_column(ForeignKey("collaborateur.id"), nullable=False)

    client = relationship("Client", back_populates="contrats")
    evenement = relationship("Evenement", uselist=False, back_populates="contrat", cascade="all, delete, delete-orphan")
    collaborateur = relationship("Collaborateur", back_populates="contrats")

    @staticmethod
    def lister_contrats() -> List["Contrat"]:
        """Renvoi la liste de tous les contrats"""
        return(ContratQueries.lister_contrats_dao(Contrat))
    

    @staticmethod
    def lister_contrats_par_id(contrat_id) -> List["Contrat"]:
        """Renvoi la liste de tous les contrats en fonction de leur id"""
        return(ContratQueries.lister_contrats_par_id_dao(Contrat, contrat_id))
    
    @staticmethod
    def lister_contrats_join_collaborateur_join_client() -> List["Contrat"]:
        """Renvoi la liste de tous les contrats avec collaborateur et client associés"""
        return(ContratQueries.lister_contrats_join_collaborateur_join_client_dao(Contrat))
    

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_signature(signature) -> List["Contrat"]:
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par signature"""
        return(ContratQueries.lister_contrats_join_collaborateur_join_client_signature_dao(Contrat, signature))
    
    @staticmethod
    def lister_contrats_join_collaborateur_join_client_paye() -> List["Contrat"]:
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par si payé"""
        return(ContratQueries.lister_contrats_join_collaborateur_join_client_paye_dao(Contrat))
    
    @staticmethod
    def lister_contrats_join_collaborateur_join_client_non_paye() -> List["Contrat"]:
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par si non payé"""
        return(ContratQueries.lister_contrats_join_collaborateur_join_client_non_paye_dao(Contrat))
    
    @staticmethod
    def lister_contrats_join_collaborateur_join_client_par_client(client_id) -> List["Contrat"]:
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par client"""
        return(ContratQueries.lister_contrats_join_collaborateur_join_client_par_client_dao(Contrat, client_id))