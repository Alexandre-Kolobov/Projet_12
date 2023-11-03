from dao.base import ouvrir_session, close_session

class ClientQueries:

    @staticmethod
    def lister_clients_dao(model_class):
        """Renvoi la liste des clients"""
        session = ouvrir_session()
        clients = session.query(model_class).all()
        close_session(session)
        
        return clients