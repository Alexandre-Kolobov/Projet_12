from dao.base import ouvrir_session, close_session, add_session, commit_session


class RoleQueries:

    @staticmethod
    def lister_roles_dao(model_class):
        """Renvoi la liste de tous les roles"""
        session = ouvrir_session()
        roles = session.query(model_class).all()
        close_session(session)

        return roles

    @staticmethod
    def ajouter_role_dao(role):
        session = ouvrir_session()
        add_session(session, role)
        commit_session(session)
        close_session(session)

    @staticmethod
    def lister_roles_par_id_dao(model_class, role_id):
        """Renvoi la liste de tous les roles par id"""
        session = ouvrir_session()
        roles = session.query(model_class).filter(model_class.id == role_id).all()
        close_session(session)

        return roles

    @staticmethod
    def lister_roles_par_name_dao(model_class, role_name):
        """Renvoi la liste de tous les roles en fonction de leur nom"""
        session = ouvrir_session()
        roles = session.query(model_class).filter(model_class.role_name == role_name).all()
        close_session(session)

        return roles
