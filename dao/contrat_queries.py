from dao.base import ouvrir_session, close_session
from sqlalchemy.orm import joinedload


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

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_dao(model_class):
        """Renvoi la liste de tous les contrats avec collaborateur et client associés"""
        session = ouvrir_session()
        contrat = (
            session.query(model_class)
            .options(joinedload(model_class.collaborateur), joinedload(model_class.client))
            .order_by(model_class.id).all()
        )

        close_session(session)
        return contrat

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_signature_dao(model_class, signature):
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par signature"""
        session = ouvrir_session()
        contrat = (
            session.query(model_class)
            .options(joinedload(model_class.collaborateur), joinedload(model_class.client))
            .filter(model_class.statut_signe == signature)
            .order_by(model_class.id).all()
        )

        close_session(session)
        return contrat

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_paye_dao(model_class):
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par si payé"""
        session = ouvrir_session()
        contrat = (
            session.query(model_class)
            .options(joinedload(model_class.collaborateur), joinedload(model_class.client))
            .filter(model_class.reste_a_payer == 0)
            .order_by(model_class.id).all()
        )

        close_session(session)
        return contrat

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_non_paye_dao(model_class):
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par si non payé"""
        session = ouvrir_session()
        contrat = (
            session.query(model_class)
            .options(joinedload(model_class.collaborateur), joinedload(model_class.client))
            .filter(model_class.reste_a_payer != 0)
            .order_by(model_class.id).all()
        )

        close_session(session)
        return contrat

    @staticmethod
    def lister_contrats_join_collaborateur_join_client_par_client_dao(model_class, client_id):
        """Renvoi la liste de tous les contrats avec collaborateur et client associés filtré par client"""
        session = ouvrir_session()
        contrat = (
            session.query(model_class)
            .options(joinedload(model_class.collaborateur), joinedload(model_class.client))
            .filter(model_class.client_id == client_id)
            .order_by(model_class.id).all()
        )

        close_session(session)
        return contrat
