import pytest
from sqlalchemy import create_engine
from dao.base import Base
from sqlalchemy.orm import sessionmaker
import configparser
from models.collaborateur import Collaborateur
from models.role import Role
from models.client import Client
from models.evenement import Evenement
from models.contrat import Contrat
import datetime


@pytest.fixture()
def collaborateur_gestionnaire():
    valid_collaborateur_gestionnaire = Collaborateur(
        nom="Einstein",
        prenom="Albert",
        email="ae@gmail.com",
        telephone=555,
        mot_de_passe="$2b$12$meTMpjI9L6RNMTb1ahpHkeGi5NQy3U5SLM2kT3oP0HK9cny4yLEz2",
        role_id=1
    )
    return (valid_collaborateur_gestionnaire)


@pytest.fixture()
def collaborateur_commercial():
    valid_collaborateur_commercial = Collaborateur(
        nom="Isaac",
        prenom="Newton",
        email="ie@gmail.com",
        telephone=555,
        mot_de_passe="$2b$12$meTMpjI9L6RNMTb1ahpHkeGi5NQy3U5SLM2kT3oP0HK9cny4yLEz2",
        role_id=2
    )
    return (valid_collaborateur_commercial)


@pytest.fixture()
def collaborateur_support():
    valid_collaborateur_support = Collaborateur(
        nom="Nicolaus",
        prenom="Copernicus",
        email="nc@gmail.com",
        telephone=555,
        mot_de_passe="$2b$12$meTMpjI9L6RNMTb1ahpHkeGi5NQy3U5SLM2kT3oP0HK9cny4yLEz2",
        role_id=3
    )
    return (valid_collaborateur_support)


@pytest.fixture()
def role_gestionnaire():
    valid_role_gestionnaire = Role(
        role_name="gestion",
    )
    return (valid_role_gestionnaire)


@pytest.fixture()
def role_commercial():
    valid_role_commercial = Role(
        role_name="commercial",
    )
    return (valid_role_commercial)


@pytest.fixture()
def role_support():
    valid_role_support = Role(
        role_name="support",
    )
    return (valid_role_support)


@pytest.fixture()
def client():
    valid_client = Client(
        nom="Oppenheimer",
        prenom="Robert",
        email="or@gmail.com",
        telephone=555,
        entreprise="Bombe Atomic SAS",
        date_creation=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        collaborateur_id=2
    )
    return (valid_client)


@pytest.fixture()
def contrat():
    valid_contrat = Contrat(
        montant_total=100,
        reste_a_payer=50,
        date_creation=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        statut_signe=False,
        client_id=1,
        collaborateur_id=2
    )
    return (valid_contrat)


@pytest.fixture()
def evenement():
    valid_evenement = Evenement(
        date_debut=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        date_fin=datetime.datetime(2025, 10, 5, 13, 00, 00).strftime("%d/%m/%Y %H:%M:%S"),
        location_pays="France",
        location_ville="Paris",
        location_rue="Colbert",
        location_num_rue=55,
        location_cp=75000,
        attendees=100,
        notes="Party time",
        contrat_id=1,
        collaborateur_id=3
    )
    return (valid_evenement)


@pytest.fixture()
def db_session(
    collaborateur_gestionnaire,
    collaborateur_commercial,
    collaborateur_support,
    role_gestionnaire,
    role_commercial,
    role_support,
    client,
    contrat,
    evenement
):

    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    dbparam = config_obj["postgresql"]

    user = dbparam["user_epic"]
    password = dbparam["password_epic"]
    host = dbparam["host"]
    db_name = dbparam["db_name_test"]

    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}', echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([
        role_gestionnaire,
        role_commercial,
        role_support,
        collaborateur_gestionnaire,
        collaborateur_commercial,
        collaborateur_support,
        client,
        contrat,
        evenement
    ])

    session.commit()

    yield session

    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture()
def pass_function():
    pass
