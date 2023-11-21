from dao.contrat_queries import ContratQueries
from models.contrat import Contrat
import pytest
from sqlalchemy.orm import joinedload


@pytest.fixture()
def mocks(mocker, db_session, pass_function):
    mock_ouvrir_session = mocker.patch('dao.contrat_queries.ouvrir_session', return_value=db_session)
    mock_close_session = mocker.patch("dao.contrat_queries.close_session", return_value=pass_function)

    return mock_ouvrir_session, mock_close_session


def test_should_return_all_contrats(db_session, mocks):
    """Doit retourner une liste des tous les contrats join collaborateur et client"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_join_collaborateur_join_client_dao(Contrat)
    contrats = (
            db_session.query(Contrat)
            .options(joinedload(Contrat.collaborateur), joinedload(Contrat.client))
            .order_by(Contrat.id).all()
        )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats


def test_should_return_all_contrats_by_signature(db_session, mocks):
    """Doit retourner une liste des tous les contrats join collaborateur et client filtré par signature """
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_join_collaborateur_join_client_signature_dao(Contrat, True)
    contrats = (
            db_session.query(Contrat)
            .options(joinedload(Contrat.collaborateur), joinedload(Contrat.client))
            .filter(Contrat.statut_signe is True)
            .order_by(Contrat.id).all()
        )
    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats


def test_should_return_all_contrats_paid(db_session, mocks):
    """Doit retourner une liste des tous les contrats join collaborateur et client payé """
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_join_collaborateur_join_client_paye_dao(Contrat)
    contrats = (
            db_session.query(Contrat)
            .options(joinedload(Contrat.collaborateur), joinedload(Contrat.client))
            .filter(Contrat.reste_a_payer == 0)
            .order_by(Contrat.id).all()
        )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats


def test_should_return_all_contrats_not_paid(db_session, mocks):
    """Doit retourner une liste des tous les contrats join collaborateur et client non payé """
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_join_collaborateur_join_client_non_paye_dao(Contrat)
    contrats = (
            db_session.query(Contrat)
            .options(joinedload(Contrat.collaborateur), joinedload(Contrat.client))
            .filter(Contrat.reste_a_payer != 0)
            .order_by(Contrat.id).all()
        )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats


def test_should_return_all_contrats_per_client(db_session, mocks):
    """Doit retourner une liste des tous les contrats join collaborateur et client filtrés par client """
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_join_collaborateur_join_client_par_client_dao(Contrat, 1)
    contrats = (
            db_session.query(Contrat)
            .options(joinedload(Contrat.collaborateur), joinedload(Contrat.client))
            .filter(Contrat.client_id == 1)
            .order_by(Contrat.id).all()
        )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats


def test_should_return_all_contrats_by_id(db_session, mocks):
    """Doit retourner une liste des tous les contrats par id"""
    mock_ouvrir_session, mock_close_session = mocks

    sut = ContratQueries.lister_contrats_par_id_dao(Contrat, 1)
    contrats = (
            db_session.query(Contrat).filter(Contrat.id == 1).all()
        )

    assert mock_ouvrir_session.call_count == 1
    assert mock_close_session.call_count == 1

    assert sut == contrats
