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

    Role.initialiser_roles(roles)

    assert mock.call_count == len(roles)  # Pour confirmer appel au mock

    for i in range(len(roles)):
        # mock.call_args_list[i][0][0]
        #  [i] un call
        #  [0] - argument de call sous forme de cortege
        #  [0] - 1ere argumpent dans cortege

        assert mock.call_args_list[i][0][0].role_name == roles[i]


def test_should_return_list_of_roles_by_role_name(mocker, role_gestionnaire, role_commercial, role_support):
    """Verifier que la fonction Role.lister_roles_par_nom()
    passe les arguments correctemments à la fonction RoleQueries.lister_roles_par_name_dao"""
    roles = [role_gestionnaire, role_commercial, role_support]

    def lister_roles_par_name_dao(roles):
        return [roles[0]]

    mock = mocker.patch('models.role.RoleQueries.lister_roles_par_name_dao', return_value=lister_roles_par_name_dao(roles))
    role_name = role_gestionnaire.role_name
    sut = Role.lister_roles_par_nom(role_name)
    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == 1


def test_should_return_list_of_roles_by_id(mocker, role_gestionnaire, role_commercial, role_support):
    """Verifier que la fonction Role.lister_roles_par_id()
    passe les arguments correctemments à la fonction RoleQueries.lister_roles_par_id_dao"""
    roles = [role_gestionnaire, role_commercial, role_support]

    def lister_roles_par_id_dao(roles):
        return [roles[0]]

    mock = mocker.patch('models.role.RoleQueries.lister_roles_par_id_dao', return_value=lister_roles_par_id_dao(roles))
    role_gestionnaire.role_id = 1
    role_id = role_gestionnaire.role_id
    sut = Role.lister_roles_par_id(role_id)
    mock.assert_called_once_with(Role, role_id)  # Si ne retourne pas AssertionError c'est ok
    assert mock.call_count == 1  # Pour confirmer appel au mock
    assert len(sut) == 1
