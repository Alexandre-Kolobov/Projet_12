from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import configparser


# Recuperation de login et mdp dans un fichier .ini
config_obj = configparser.ConfigParser()
config_obj.read("config.ini")
dbparam = config_obj["postgresql"]

user = dbparam["user_admin"]
password = dbparam["password_admin"]
host = dbparam["host"]

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/epic_crm', echo=False)

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


def commit_session(session):
    """Permet commit une sessions"""
    session.commit()


def close_session(session):
    """Permet fermer une sessions"""
    session.close()


def valider_session(obj):
    """Regroupe actions d'ouverture, add, commit et close"""
    session = ouvrir_session()
    add_session(session, obj)
    commit_session(session)
    close_session(session)