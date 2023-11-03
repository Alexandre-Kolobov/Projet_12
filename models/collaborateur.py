from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dao.base import Base
from dao.collaborateur_queries import CollaborateurQueries
import bcrypt
from typing import List, Union
import configparser
import jwt
from jwt.exceptions import InvalidSignatureError


class Collaborateur(Base):
    __tablename__ = "collaborateur"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    telephone: Mapped[int] = mapped_column(Integer, nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(String(100), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=False)

    role = relationship("Role", back_populates="collaborateurs")
    clients = relationship("Client", back_populates="collaborateur")
    contrats = relationship("Contrat", back_populates="collaborateur")
    evenements = relationship("Evenement", back_populates="collaborateur")


    def __repr__(self):
        return (f"id{self.id} {self.nom} {self.prenom}")
    

    def hacher_mot_de_passe(self) -> None:
        """Hachage et sel de mot de passe"""
        mot_de_passe_hache = bcrypt.hashpw(self.mot_de_passe.encode('utf-8'), bcrypt.gensalt())
        self.mot_de_passe = mot_de_passe_hache.decode('utf-8')


    def verifier_mot_de_passe(self, mot_de_passe: str) -> bool:
        """Controle de hache de mot de passe"""
        return bcrypt.checkpw(mot_de_passe.encode('utf-8'), self.mot_de_passe.encode('utf-8'))
    

    def generer_token(self) -> str:
        """Genere JWT"""
        config_obj = configparser.ConfigParser()
        config_obj.read("config.ini")
        jwt_param = config_obj["jwt"]

        secret = jwt_param["secret"]

        payload_data = {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "role_id": self.role_id,
        }

        token = jwt.encode(
            payload=payload_data,
            key=secret
        )

        return token


    @staticmethod
    def verifier_token(token:str) -> bool:
        """Decode token et retourn son payload"""
        config_obj = configparser.ConfigParser()
        config_obj.read("config.ini")
        jwt_param = config_obj["jwt"]

        secret = jwt_param["secret"]
        header_data = jwt.get_unverified_header(token)

        try:
            payload_data = jwt.decode(jwt=token, key=secret, algorithms=header_data["alg"])
            return True
        
        except InvalidSignatureError:
            return False

    @staticmethod
    def lister_collaborateurs() -> List["Collaborateur"]:
        """Renvoi la liste de tous les collaborateurs"""
        return(CollaborateurQueries.lister_collaborateurs_dao(Collaborateur))


    @staticmethod
    def selectionner_collaborateurs_par_nom_prenom(nom, prenom) -> List["Collaborateur"]:
        """Renvoi la liste des collaborateurs en fonction du nom prenom indiqué"""
        return(CollaborateurQueries.selectionner_collaborateurs_par_nom_prenom_dao(Collaborateur, nom, prenom))


    @staticmethod
    def selectionner_collaborateurs_par_id(id) -> List["Collaborateur"]:
        """Renvoi la liste des collaborateurs en fonction de leur id"""
        return(CollaborateurQueries.selectionner_collaborateurs_par_id_dao(Collaborateur, id))


    @staticmethod
    def selectionner_collaborateurs_par_role(role_id) -> List["Collaborateur"]:
        """Renvoi la liste des collaborateurs en fonction de leur role"""
        return(CollaborateurQueries.selectionner_collaborateurs_par_role_dao(Collaborateur, role_id))


    @staticmethod
    def selectionner_collaborateurs_par_email(email) -> List["Collaborateur"]:
        """Renvoi la liste des collaborateurs en fonction de leur email"""
        return(CollaborateurQueries.selectionner_collaborateurs_par_email_dao(Collaborateur, email))
    