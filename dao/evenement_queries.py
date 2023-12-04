from dao.base import ouvrir_session, close_session
from sqlalchemy.orm import joinedload
from models.contrat import Contrat


class EvenementQueries:

    @staticmethod
    def lister_evenements_dao(model_class):
        """Renvoi la liste des evenements"""
        session = ouvrir_session()
        evenements = session.query(model_class).all()
        close_session(session)

        return evenements

    @staticmethod
    def lister_evenements_join_contrat_collaborateurs_client_dao(model_class):
        """Renvoi la liste des evenements join contrat client et collaborateurs"""
        session = ouvrir_session()
        evenements = (
            session.query(model_class)
            .options(
                joinedload(model_class.contrat).joinedload(Contrat.client),
                joinedload(model_class.contrat).joinedload(Contrat.collaborateur),
                joinedload(model_class.collaborateur))
            .order_by(model_class.id).all()
            )
        close_session(session)

        return evenements

    @staticmethod
    def lister_evenements_par_collaborateur_dao(model_class, id):
        """Renvoi la liste des evenements join contrat client et collaborateurs"""
        session = ouvrir_session()
        evenements = (
            session.query(model_class)
            .options(
                joinedload(model_class.contrat).joinedload(Contrat.client),
                joinedload(model_class.contrat).joinedload(Contrat.collaborateur),
                joinedload(model_class.collaborateur))
            .filter(model_class.collaborateur_id == id)
            .order_by(model_class.id).all()
            )
        close_session(session)

        return evenements

    @staticmethod
    def lister_evenements_par_id_dao(model_class, id):
        """Renvoi la liste des evenements"""
        session = ouvrir_session()
        evenements = session.query(model_class).filter(model_class.id == id).all()
        close_session(session)

        return evenements

    @staticmethod
    def lister_evenements_sans_collaborateur_dao(model_class):
        """Renvoi la liste des evenements join contrat client et collaborateurs"""
        session = ouvrir_session()
        evenements = (
            session.query(model_class)
            .options(
                joinedload(model_class.contrat).joinedload(Contrat.client),
                joinedload(model_class.contrat).joinedload(Contrat.collaborateur),
                joinedload(model_class.collaborateur))
            .filter(model_class.collaborateur_id == None)
            .order_by(model_class.id).all()
            )
        close_session(session)

        return evenements
