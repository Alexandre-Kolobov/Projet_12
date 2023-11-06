from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dao.base import Base
from datetime import datetime
from typing import Optional
from typing import List
from dao.client_queries import ClientQueries


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    telephone: Mapped[int] = mapped_column(Integer, nullable=False)
    entreprise: Mapped[str] = mapped_column(String(250), nullable=False)
    date_creation: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_update: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    collaborateur_id: Mapped[int] = mapped_column(ForeignKey("collaborateur.id"), nullable=False)

    collaborateur = relationship("Collaborateur", back_populates="clients")
    contrats = relationship("Contrat", back_populates="client", cascade="all, delete, delete-orphan")


    @staticmethod
    def lister_clients() -> List["Client"]:
        """Renvoi la liste des clients"""
        return(ClientQueries.lister_clients_dao(Client))

    
    @staticmethod
    def clients_as_list_of_dict(clients:list["Client"]) -> List[dict]:
        """Renvoi les info des clients sous form de list des dictionnaires"""
        clients_as_list_of_dict = [{client.id:f"{client.nom} {client.prenom} - {client.entreprise}"} for client in clients]
        return (clients_as_list_of_dict)