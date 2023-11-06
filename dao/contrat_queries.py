from dao.base import ouvrir_session, close_session

class ContratQueries:

    @staticmethod
    def lister_contrats_dao(model_class):
        """Renvoi la liste des contrat"""
        session = ouvrir_session()
        contrats = session.query(model_class).all()
        close_session(session)
        
        return contrats
    

    @staticmethod
    def lister_contrats_par_id_dao(model_class, contrat_id):
        """Renvoi la liste de tous les contrats par id"""
        session = ouvrir_session()
        roles = session.query(model_class).filter(model_class.id == contrat_id).all()
        close_session(session)
        
        return roles