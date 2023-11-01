from dao.base import ouvrir_session, close_session

class RoleQueries:

    @staticmethod
    def lister_roles_dao(model_class):
        """Renvoi la liste de tous les roles"""
        session = ouvrir_session()
        roles = session.query(model_class).all()
        close_session(session)
        
        return roles