from dao.base import ouvrir_session, close_session
from sqlalchemy.orm import joinedload


class ClientQueries:

    @staticmethod
    def lister_clients_dao(model_class):
        """Renvoi la liste des clients"""
        session = ouvrir_session()
        clients = session.query(model_class).all()
        close_session(session)

        return clients

    @staticmethod
    def lister_clients_join_collaborateur_dao(model_class):
        """Renvoi la liste de tous les clients avec leur collaborateur associé"""
        session = ouvrir_session()
        clients = session.query(model_class).options(joinedload(model_class.collaborateur)).order_by(model_class.id).all()
        close_session(session)
        return clients

    @staticmethod
    def selectionner_client_par_id_dao(model_class, id):
        """Renvoi la liste des collaborateurs en fonction de leur id"""
        session = ouvrir_session()
        clients = session.query(model_class).filter(model_class.id == id).all()
        close_session(session)

        return clients
