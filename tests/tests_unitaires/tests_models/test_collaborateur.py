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

    # def mock_selectionner_collaborateurs_par_email_dao(collaborateurs):
    #     return collaborateurs

    mock = mocker.patch(
        'models.collaborateur.CollaborateurQueries.selectionner_collaborateurs_par_email_dao',
        return_value=collaborateurs
        )

    sut = Collaborateur.selectionner_collaborateurs_par_email(email)

    mock.assert_called_once_with(Collaborateur, email) # si ne retourne pas AssertionError c'est ok 
    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == len(collaborateurs)


def test_should_retourn_list_of_collaborateurs_join_role_ordered_by_id(mocker):
    """Verifier que la fonction Collaborateur.lister_collaborateurs_join_roles()
    appele fonction CollaborateurQueries.lister_collaborateurs_join_roles_dao
    avec des bons arguments"""

    mock = mocker.patch('models.collaborateur.CollaborateurQueries.lister_collaborateurs_join_roles_dao')

    sut = Collaborateur.lister_collaborateurs_join_roles()

    mock.assert_called_once_with(Collaborateur) # si ne retourne pas AssertionError c'est ok 
    assert mock.call_count == 1  # Pour confirmer appel au mock
   