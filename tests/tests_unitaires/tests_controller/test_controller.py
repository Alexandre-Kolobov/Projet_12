from controller.controller import Controller
from permissions.permissions_manager import Permissions

def test_should_return_true_if_list_non_vide(mocker):
    """Verifie que la fonction Controller.roles_existent_dans_db retourn true si roles existent"""
    mock = mocker.patch('controller.controller.Role.lister_roles', return_value=[1,2,3])
    sut = Controller.roles_existent_dans_db()

    assert mock.call_count == 1
    assert sut == True


def test_should_return_false_if_list_vide(mocker):
    """Verifie que la fonction Controller.roles_existent_dans_db retourn false si roles n'existent pas"""
    mock = mocker.patch('controller.controller.Role.lister_roles', return_value=[])
    sut = Controller.roles_existent_dans_db()

    assert mock.call_count == 1
    assert sut == False

def test_should_pass_list_with_arguments(mocker):
    """Verifie que la fonction Controller.initialiser_roles fait l'appel à Role.initialiser_roles corerctemments"""
    mock = mocker.patch('controller.controller.Role.initialiser_roles') 
    Controller.initialiser_roles()

    assert mock.call_count == 1

    expected_roles = [role.value for role in Permissions.RolesEnum]
    assert mock.call_args_list[0][0][0] == expected_roles



    
