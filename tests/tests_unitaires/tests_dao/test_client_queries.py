from dao.client_queries import ClientQueries
from models.client import Client
import pytest
from sqlalchemy.orm import joinedload


@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.client_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.client_queries.close_session", return_value=pass_function)
    
    return mock_ouvrir_session, mock_close_session


def test_should_return_all_clients(db_session, mocks):
    """Doit retourner une liste des tous les clients"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = ClientQueries.lister_clients_dao(Client)
    contrats = (
            db_session.query(Client).all()
            )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats