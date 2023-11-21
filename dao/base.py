from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import configparser


# Recuperation de login et mdp dans un fichier .ini
config_obj = configparser.ConfigParser()
config_obj.read("config.ini")
dbparam = config_obj["postgresql"]

user = dbparam["user_epic"]
password = dbparam["password_epic"]
host = dbparam["host"]
db_name = dbparam["db_name"]

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}', echo=False)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def creer_database_tables():
    """Permet verifier l'existance des tables ou de creer les tables a partir des modeles"""
    Base.metadata.create_all(engine)


def supprimer_database_tables():
    """Permet de supprimer toutes les tables"""
    Base.metadata.drop_all(engine)


def ouvrir_session():
    """Permet d'ouvrir une session"""
    session = Session()
    return session


def add_session(session, obj):
    """Permet d'ajouter un objet dans la session en cours"""
    session.add(obj)


def delete_session(session, obj):
    """Permet de supprimer un objet de la session en cours"""
    session.delete(obj)


def commit_session(session):
    """Permet commit une sessions"""
    session.commit()


def close_session(session):
    """Permet fermer une sessions"""
    session.close()


def valider_sessions_supprimer_objet(obj):
    """Regroupe actions d'ouverture, suppression, commit et close"""
    session = ouvrir_session()
    delete_session(session, obj)
    commit_session(session)
    close_session(session)


def valider_session(obj):
    """Regroupe actions d'ouverture, add, commit et close"""
    session = ouvrir_session()
    add_session(session, obj)
    commit_session(session)
    close_session(session)
