from dao.base import ouvrir_session, close_session

class CollaborateurQueries:

    @staticmethod
    def lister_collaborateurs_dao(model_class):
        """Renvoi la liste de tous les collaborateurs"""
        session = ouvrir_session()
        collaborateurs = session.query(model_class).all()
        close_session(session)
        
        return collaborateurs
    
    @staticmethod
    def selectionner_collaborateurs_par_nom_prenom_dao(model_class, nom, prenom):
        """Renvoi la liste des collaborateurs en fonction du nom prenom indiqué"""
        session = ouvrir_session()
        collaborateurs = session.query(model_class).filter(model_class.nom == nom, model_class.prenom == prenom).all()
        close_session(session)
        
        return collaborateurs
    
    @staticmethod
    def selectionner_collaborateurs_par_id_dao(model_class, id):
        """Renvoi la liste des collaborateurs en fonction de leur id"""
        session = ouvrir_session()
        collaborateurs = session.query(model_class).filter(model_class.id == id).all()
        close_session(session)
        
        return collaborateurs
    
    @staticmethod
    def selectionner_collaborateurs_par_role_dao(model_class, role_id):
        """Renvoi la liste des collaborateurs en fonction de leur role"""
        session = ouvrir_session()
        collaborateurs = session.query(model_class).filter(model_class.role_id == role_id).all()
        close_session(session)
        
        return collaborateurs
    
    @staticmethod
    def selectionner_collaborateurs_par_email_dao(model_class, email):
        """Renvoi la liste des collaborateurs en fonction de leur email"""
        session = ouvrir_session()
        collaborateurs = session.query(model_class).filter(model_class.email == email).all()
        close_session(session)
        
        return collaborateurs