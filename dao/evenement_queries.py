from dao.base import ouvrir_session, close_session

class EvenementQueries:

    @staticmethod
    def lister_evenements_dao(model_class):
        """Renvoi la liste des evenements"""
        session = ouvrir_session()
        evenements = session.query(model_class).all()
        close_session(session)
        
        return evenements