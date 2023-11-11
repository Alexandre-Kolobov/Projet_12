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