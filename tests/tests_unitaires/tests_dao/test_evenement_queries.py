from dao.evenement_queries import EvenementQueries
from models.evenement import Evenement
from models.contrat import Contrat
import pytest
from sqlalchemy.orm import joinedload


@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.evenement_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.evenement_queries.close_session", return_value=pass_function)
    
    return mock_ouvrir_session, mock_close_session


def test_should_return_all_evenements_with_collaborateur_contrat_client(db_session, mocks):
    """Doit retourner une liste des tous les evenement join collaborateur, client et contrat"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = EvenementQueries.lister_evenements_join_contrat_collaborateurs_client_dao(Evenement)
    evenements = (
            db_session.query(Evenement)
            .options(
                joinedload(Evenement.contrat).joinedload(Contrat.client),
                joinedload(Evenement.contrat).joinedload(Contrat.collaborateur),
                joinedload(Evenement.collaborateur))
            .order_by(Evenement.id).all()
            )
    

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == evenements


def test_should_return_all_evenements_with_collaborateur_contrat_client_filtered_by_id(db_session, mocks):
    """Doit retourner une liste des tous les evenement join collaborateur, client et contrat"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = EvenementQueries.lister_evenements_par_collaborateur_dao(Evenement, "1")
    evenements = (
        db_session.query(Evenement)
        .options(
            joinedload(Evenement.contrat).joinedload(Contrat.client),
            joinedload(Evenement.contrat).joinedload(Contrat.collaborateur),
            joinedload(Evenement.collaborateur))
        .filter(Evenement.collaborateur_id=="1")
        .order_by(Evenement.id).all()
        )
    

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == evenements