from controller.controller import Controller
from permissions.permissions_manager import Permissions
from models.role import Role
import bcrypt

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
    """Verifie que la fonction Controller.initialiser_roles fait l'appel à Role.initialiser_roles correctement"""
    mock = mocker.patch('controller.controller.Role.initialiser_roles') 
    Controller.initialiser_roles()

    assert mock.call_count == 1

    expected_roles = [role.value for role in Permissions.RolesEnum]
    assert mock.call_args_list[0][0][0] == expected_roles


def test_should_return_true_if_collaborateur_exists_in_db(
        mocker,
        collaborateur_gestionnaire,
        collaborateur_commercial,
        collaborateur_support
        ):
    """Verifie que la fonction Controller.collaborateurs_existent_dans_db fait return bool correctement"""
    mock = mocker.patch(
        'controller.controller.Collaborateur.lister_collaborateurs',
        return_value=[
            collaborateur_gestionnaire,
            collaborateur_commercial,
            collaborateur_support]
        )

    sut = Controller.collaborateurs_existent_dans_db()
    assert mock.call_count == 1
    assert sut == True


def test_should_return_false_if_collaborateur_doesnt_exist_in_db(mocker):
    """Verifie que la fonction Controller.collaborateurs_existent_dans_db fait return bool correctement"""
    mock = mocker.patch('controller.controller.Collaborateur.lister_collaborateurs', return_value=[])

    sut = Controller.collaborateurs_existent_dans_db()
    assert mock.call_count == 1
    assert sut == False

def test_should_create_collaborateur_instance_if_first_user_doesnt_exists(mocker):
        """Verifie que la fonction Controller.enregistrer_collaborateur enregistre premiere collaborateur comme gestionnaire"""

        mock_prenom = mocker.patch(
             'controller.controller.ViewCollaborateur.entrer_prenom_collaborateur',
             return_value="Steve"
             )
        
        mock_nom = mocker.patch(
             'controller.controller.ViewCollaborateur.entrer_nom_collaborateur',
             return_value="Jobs"
             )
        
        mock_email = mocker.patch(
             'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
             return_value="sj@gmail.com"
             )
        

        mock_telephone = mocker.patch(
             'controller.controller.ViewCollaborateur.entrer_telephone_collaborateur',
             return_value=555
             )
        
        mot_de_pass = "123456"
        return_hache=bcrypt.hashpw(mot_de_pass.encode('utf-8'), bcrypt.gensalt())
        
        mock_mot_de_passe = mocker.patch(
             'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
             return_value=return_hache
             )
        
        role_gestionnaire = Role(id=1, role_name="gestion")
        role_commercial = Role(id=2, role_name="commercial")
        role_support = Role(id=3, role_name="support")
        
        mock_roles = mocker.patch(
             'controller.controller.Role.lister_roles',
             return_value=[role_gestionnaire, role_commercial, role_support]
             )
        
        mock_lister_roles_par_nom = mocker.patch(
             'controller.controller.Role.lister_roles_par_nom',
             return_value=[role_gestionnaire]
             )
        
        mock_hacher_mot_de_pass = mocker.patch('controller.controller.Collaborateur.hacher_mot_de_passe')

        
        mock_valider_session = mocker.patch("controller.controller.valider_session")
        
        Controller.enregistrer_collaborateur(False)
        assert mock_valider_session.call_count == 1
        assert mock_valider_session.call_args.args[0].prenom == "Steve"
        assert mock_valider_session.call_args.args[0].nom == "Jobs"
        assert mock_valider_session.call_args.args[0].email == "sj@gmail.com"
        assert mock_valider_session.call_args.args[0].telephone == 555
        assert mock_valider_session.call_args.args[0].mot_de_passe == return_hache
        assert mock_valider_session.call_args.args[0].role_id == 1
