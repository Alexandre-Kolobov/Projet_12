from models.collaborateur import Collaborateur
from models.role import Role
from models.client import Client
from models.contrat import Contrat
from models.evenement import Evenement

def test_role_valide(db_session):
    """Validation de modele role"""
    session = db_session
    role = session.query(Role).filter_by(role_name="gestion").first()
    assert role.role_name == "gestion"


def test_collaborateur_valide(db_session):
    session = db_session
    collaborateur = session.query(Collaborateur).filter_by(email="ae@gmail.com").first()
    assert collaborateur.nom == "Einstein"
    assert collaborateur.prenom == "Albert"
    assert collaborateur.email == "ae@gmail.com"
    assert collaborateur.telephone == 555
    assert collaborateur.mot_de_passe == "$2b$12$meTMpjI9L6RNMTb1ahpHkeGi5NQy3U5SLM2kT3oP0HK9cny4yLEz2"

    role = session.query(Role).filter_by(role_name="gestion").first()
    assert collaborateur.role_id == collaborateur.role.id


def test_client_valide(db_session):
    session = db_session
    client = session.query(Client).filter_by(email="or@gmail.com").first()

    assert client.nom == "Oppenheimer"
    assert client.prenom == "Robert"
    assert client.email == "or@gmail.com"
    assert client.telephone == 555
    assert client.entreprise == "Bombe Atomic SAS"
    role_obj = session.query(Role).filter_by(role_name="commercial").first()
    
    assert client.collaborateur.role.id == role_obj.id


def test_contrat_valide(db_session):
    session = db_session
    contrat = session.query(Contrat).filter_by(montant_total=100).first()
    assert contrat.montant_total == 100
    assert contrat.reste_a_payer == 50
    assert contrat.statut_signe == False
    assert contrat.client_id == 1
    assert contrat.collaborateur_id == 2


def test_evenement_valide(db_session):
    session = db_session
    evenement = session.query(Evenement).filter_by(contrat_id=1).first()
    assert evenement.location_pays == "France"
    assert evenement.location_ville == "Paris"
    assert evenement.location_rue == "Colbert"
    assert evenement.location_num_rue == 55
    assert evenement.location_cp == 75000
    assert evenement.attendees == 100
    assert evenement.notes == "Party time"
    assert evenement.contrat_id == 1
    assert evenement.collaborateur_id == 3


