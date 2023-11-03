from dao.base import ouvrir_session, close_session

class ContratQueries:

    @staticmethod
    def lister_contrats_dao(model_class):
        """Renvoi la liste des contrat"""
        session = ouvrir_session()
        contrats = session.query(model_class).all()
        close_session(session)
        
        return contrats