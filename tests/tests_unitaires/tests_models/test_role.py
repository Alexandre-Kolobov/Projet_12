from models.role import Role

def test_should_retourn_list_of_roles(mocker, role_gestionnaire, role_commercial, role_support):
    """Verifier que la fonction Role.lister_roles() return une liste correctemment"""
    roles = [role_gestionnaire, role_commercial, role_support]

    def mock_lister_roles_dao(roles):
        return roles
    
    mock = mocker.patch('models.role.RoleQueries.lister_roles_dao', return_value=mock_lister_roles_dao(roles))
    sut = Role.lister_roles()
    
    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == len(roles)


def test_should_add_roles_to_db(mocker):
    """Verifier que la fonction Role.initialiser_roles()
    passe les arguments correctemments à la fonction RoleQueries.ajouter_role_dao"""

    roles = ["test_1", "test_2", "test_3"]

    # Pour mocker l'appel au fonction
    # Cela permet de compter combien de fois cette fonction a été appelé
    mock = mocker.patch('models.role.RoleQueries.ajouter_role_dao') 

    sut = Role.initialiser_roles(roles)

    assert mock.call_count == len(roles)  # Pour confirmer appel au mock
    
    for i in range(len(roles)):
        # mock.call_args_list[i][0][0]
        #  [i] un call
        #  [0] - argument de call sous forme de cortege
        #  [0] - 1ere argumpent dans cortege

        assert mock.call_args_list[i][0][0].role_name == roles[i]