from models.collaborateur import Collaborateur


def test_should_retourn_list_of_collaborateurs(
        mocker,
        collaborateur_gestionnaire,
        collaborateur_commercial,
        collaborateur_support
        ):
    """Verifier que la fonction Collaborateur.lister_collaborateurs() return une liste correctemment"""
    collaborateurs = [collaborateur_gestionnaire, collaborateur_commercial, collaborateur_support]

    def mock_lister_collaborateurs(collaborateurs):
        return collaborateurs

    mock = mocker.patch(
        'models.collaborateur.CollaborateurQueries.lister_collaborateurs_dao',
        return_value=mock_lister_collaborateurs(collaborateurs)
        )
    sut = Collaborateur.lister_collaborateurs()

    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == len(collaborateurs)


def test_should_retourn_list_of_collaborateurs_filtered_by_email(
        mocker,
        collaborateur_gestionnaire
        ):
    """Verifier que la fonction Collaborateur.selectionner_collaborateurs_par_email()
    appele fonction CollaborateurQueries.selectionner_collaborateurs_par_email_dao
    avec des bons arguments"""

    email = "ae@gmail.com"
    collaborateurs = [collaborateur_gestionnaire]

    mock = mocker.patch(
        'models.collaborateur.CollaborateurQueries.selectionner_collaborateurs_par_email_dao',
        return_value=collaborateurs
        )

    sut = Collaborateur.selectionner_collaborateurs_par_email(email)

    mock.assert_called_once_with(Collaborateur, email)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == len(collaborateurs)


def test_should_retourn_list_of_collaborateurs_join_role_ordered_by_id(mocker):
    """Verifier que la fonction Collaborateur.lister_collaborateurs_join_roles()
    appele fonction CollaborateurQueries.lister_collaborateurs_join_roles_dao
    avec des bons arguments"""

    mock = mocker.patch('models.collaborateur.CollaborateurQueries.lister_collaborateurs_join_roles_dao')

    Collaborateur.lister_collaborateurs_join_roles()

    mock.assert_called_once_with(Collaborateur)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_return_list_of_collaborateurs(mocker):
    """La fonction doit retourner une liste des collaborateurs Collaborateur.selectionner_collaborateurs_par_role_id
    en applant fonction CollaborateurQueries.selectionner_collaborateurs_par_id_dao"""

    mock = mocker.patch('models.collaborateur.CollaborateurQueries.selectionner_collaborateurs_par_role_id_dao')

    Collaborateur.selectionner_collaborateurs_par_role_id(2)

    mock.assert_called_once_with(Collaborateur, 2)  # si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock


def test_should_return_list_of_dicts(collaborateur_commercial):
    """La fonction doit retourner une liste des dictionnaire des collaborateurs Collaborateur.collaborateurs_as_list_of_dict"""

    list_collaborateur = [collaborateur_commercial]
    sut = Collaborateur.collaborateurs_as_list_of_dict(list_collaborateur)

    assert sut == [{collaborateur_commercial.id:
                    f"{collaborateur_commercial.nom} {collaborateur_commercial.prenom}"}]
