from dao.role_queries import RoleQueries
from models.role import Role
import pytest

@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.role_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.role_queries.close_session", return_value=pass_function)
    
    return mock_ouvrir_session, mock_close_session


def test_should_return_all_roles(db_session, mocks):
    """Verification qu'on recuper la liste des roles correctemment"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = RoleQueries.lister_roles_dao(Role)
    roles = db_session.query(Role).all()

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1
    assert sut == roles


def test_should_add_role(db_session, mocks):
    """Verification qu'on recuper la liste des roles correctemment"""
    mock_ouvrir_session, mock_close_session = mocks

    role_name = "role_test"

    sut = Role(role_name=role_name)
    RoleQueries.ajouter_role_dao(sut)
    role_from_db = db_session.query(Role).filter(Role.role_name==role_name).first()

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1
    assert sut == role_from_db


