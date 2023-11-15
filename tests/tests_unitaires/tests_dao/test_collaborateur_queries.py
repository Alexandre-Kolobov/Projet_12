from dao.collaborateur_queries import CollaborateurQueries
from models.collaborateur import Collaborateur
import pytest
from sqlalchemy.orm import joinedload


@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.collaborateur_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.collaborateur_queries.close_session", return_value=pass_function)
    
    return mock_ouvrir_session, mock_close_session


def test_should_return_all_collaborateurs(db_session, mocks):
    """Doit retourner une liste des tous les collaborateurs"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = CollaborateurQueries.lister_collaborateurs_dao(Collaborateur)
    collaborateurs = db_session.query(Collaborateur).all()

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == collaborateurs


def test_should_return_all_collaborateurs_join_roles(db_session, mocks):
    """Doit retourner une liste des tous les collaborateurs associés à leur role"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = CollaborateurQueries.lister_collaborateurs_join_roles_dao(Collaborateur)
    collaborateurs = db_session.query(Collaborateur).options(joinedload(Collaborateur.role)).order_by(Collaborateur.id).all()

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == collaborateurs