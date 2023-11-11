from dao.collaborateur_queries import CollaborateurQueries
from models.collaborateur import Collaborateur
import pytest

@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.collaborateur_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.collaborateur_queries.close_session", return_value=pass_function)
    
    return mock_ouvrir_session, mock_close_session


def test_should_return_all_collaborateurs(db_session, mocks):

    mock_ouvrir_session, mock_close_session = mocks

    sut = CollaborateurQueries.lister_collaborateurs_dao(Collaborateur)
    collaborateurs = db_session.query(Collaborateur).all()

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == collaborateurs