from models.contrat import Contrat


def test_should_retourn_liste_of_contrats_join_collaborateur_join_client_ordered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_join_collaborateur_join_client()
    appele fonction ContratQueries.lister_contrats_join_collaborateur_join_client_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_join_collaborateur_join_client_dao')

    Contrat.lister_contrats_join_collaborateur_join_client()

    mock.assert_called_once_with(Contrat)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_contrats_join_collaborateur_join_client_filtre_par_signature_ordered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_join_collaborateur_join_client_signature()
    appele fonction ContratQueries.lister_contrats_join_collaborateur_join_client_signature_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_join_collaborateur_join_client_signature_dao')

    Contrat.lister_contrats_join_collaborateur_join_client_signature(True)

    mock.assert_called_once_with(Contrat, True)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_contrats_join_collaborateur_join_client_filter_if_paye_ordered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_join_collaborateur_join_client_paye()
    appele fonction ContratQueries.lister_contrats_join_collaborateur_join_client_paye_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_join_collaborateur_join_client_paye_dao')

    Contrat.lister_contrats_join_collaborateur_join_client_paye()

    mock.assert_called_once_with(Contrat)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_contrats_join_collaborateur_join_client_filter_if_no_paye_ordered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_join_collaborateur_join_client_non_paye()
    appele fonction ContratQueries.lister_contrats_join_collaborateur_join_client_non_paye_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_join_collaborateur_join_client_non_paye_dao')

    Contrat.lister_contrats_join_collaborateur_join_client_non_paye()

    mock.assert_called_once_with(Contrat)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_contrats_join_collaborateur_join_client_filter_by_client_ordered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_join_collaborateur_join_client_par_client()
    appele fonction ContratQueries.lister_contrats_join_collaborateur_join_client_par_client_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_join_collaborateur_join_client_par_client_dao')

    Contrat.lister_contrats_join_collaborateur_join_client_par_client(1)

    mock.assert_called_once_with(Contrat, 1)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_contrats_filtered_by_id(mocker):
    """Verifier que la fonction Contrat.lister_contrats_par_id()
    appele fonction ContratQueries.lister_contrats_par_id_dao
    avec des bons arguments"""

    mock = mocker.patch('models.contrat.ContratQueries.lister_contrats_par_id_dao')

    Contrat.lister_contrats_par_id("1")

    mock.assert_called_once_with(Contrat, "1")  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock
