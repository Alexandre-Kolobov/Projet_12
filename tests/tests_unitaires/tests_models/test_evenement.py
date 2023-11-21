from models.evenement import Evenement


def test_should_retourn_evenement_contrat_client_collaborateurs(mocker):
    """Verifier que la fonction Evenement.lister_evenements_join_contrat_collaborateurs_client()
    appele fonction EvenementQueries.lister_evenements_join_contrat_collaborateurs_client_dao
    avec des bons arguments"""

    mock = mocker.patch('models.evenement.EvenementQueries.lister_evenements_join_contrat_collaborateurs_client_dao')

    Evenement.lister_evenements_join_contrat_collaborateurs_client()

    mock.assert_called_once_with(Evenement)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_evenement_contrat_client_collaborateurs_by_support(mocker):
    """Verifier que la fonction Evenement.lister_evenements_par_collaborateur()
    appele fonction EvenementQueries.lister_evenements_par_collaborateur_dao
    avec des bons arguments"""

    mock = mocker.patch('models.evenement.EvenementQueries.lister_evenements_par_collaborateur_dao')

    Evenement.lister_evenements_par_collaborateur("1")

    mock.assert_called_once_with(Evenement, "1")  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_retourn_liste_of_evenements_filtered_by_id(mocker):
    """Verifier que la fonction Evenement.lister_evenements_par_id()
    appele fonction EvenementQueries.lister_evenements_par_id_dao
    avec des bons arguments"""

    mock = mocker.patch('models.evenement.EvenementQueries.lister_evenements_par_id_dao')

    Evenement.lister_evenements_par_id("1")

    mock.assert_called_once_with(Evenement, "1")  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock
