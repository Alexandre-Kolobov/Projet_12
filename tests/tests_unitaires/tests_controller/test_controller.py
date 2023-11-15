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


def test_should_return_none_if_wrong_email_when_authetication(mocker):
    """Verification de fonctionnment de Controller.authentication_user.
    Doit retourner None si authentification echou et appeler ViewCollaborateur.refuser_authentification.
    Dans ce cas l'authentification doit echouer car le login(email) ne permet pas de retrouver un collaborateur existant."""

    mock_email = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
    return_value="test_fails@gmail.com"
    )

    mock_password = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
    return_value="password_fails"
    )

    mock_collaborateurs = mocker.patch(
    'controller.controller.Collaborateur.selectionner_collaborateurs_par_email',
    return_value=[]
    )

    mock_refuser_authentification = mocker.patch('controller.controller.ViewCollaborateur.refuser_authentification')

    sut = Controller.authentication_user()
    assert mock_refuser_authentification.call_count == 1
    assert sut == None


def test_should_return_none_if_wrong_password_when_authetication(mocker, collaborateur_gestionnaire):
    """Verification de fonctionnment de Controller.authentication_user.
    Doit retourner None si authentification echou et appeler ViewCollaborateur.refuser_authentification.
    Dans ce cas l'authentification doit echouer car le mot de pass ne correspond pas à celui associé au login."""

    mock_email = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
    return_value="test_fails@gmail.com"
    )

    mock_password = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
    return_value="password_fails"
    )

    mock_collaborateurs = mocker.patch(
    'controller.controller.Collaborateur.selectionner_collaborateurs_par_email',
    return_value=[collaborateur_gestionnaire]
    )

    mock_verifier_mot_de_passe = mocker.patch(
    'controller.controller.Collaborateur.verifier_mot_de_passe',
    return_value=False
    )

    mock_refuser_authentification = mocker.patch('controller.controller.ViewCollaborateur.refuser_authentification')

    sut = Controller.authentication_user()
    assert mock_refuser_authentification.call_count == 1
    assert mock_verifier_mot_de_passe.call_count == 1
    assert sut == None


def test_should_return_collaborateur_if_credentials_are_ok(mocker, collaborateur_gestionnaire):
    """Verification de fonctionnment de Controller.authentication_user.
    Doit retourner collaborateur si authentification est ok."""

    mock_email = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
    return_value="ae@gmail.com"
    )

    mock_password = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
    return_value="123456"
    )
    
    mock_password = mocker.patch(
    'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
    return_value="password_fails"
    )

    mock_collaborateurs = mocker.patch(
    'controller.controller.Collaborateur.selectionner_collaborateurs_par_email',
    return_value=[collaborateur_gestionnaire]
    )

    mock_verifier_mot_de_passe = mocker.patch(
    'controller.controller.Collaborateur.verifier_mot_de_passe',
    return_value=True
    )

    sut = Controller.authentication_user()
    assert sut == collaborateur_gestionnaire

def test_should_return_true_if_collaborateur_has_autorization(mocker):
    """Verification de fonctionnment de Controller.check_authorization_permission.
    Doit retourner True si token et permissions sont ok."""

    mock_token = mocker.patch(
    'controller.controller.Collaborateur.verifier_token',
    return_value=True
    )

    mock_permissions = mocker.patch(
    'controller.controller.Permissions.verification_persmissions_de_collaborateur',
    return_value=True
    )

    sut = Controller.check_authorization_permission("test_token", "test_role", "test_permission")

    assert mock_token.call_count == 1
    assert mock_permissions.call_count == 1
    assert sut == True


def test_should_return_false_if_collaborateur_has_wrong_token(mocker):
    """Verification de fonctionnment de Controller.check_authorization_permission.
    Doit retourner False si token n'est pas valide."""

    mock_token = mocker.patch(
    'controller.controller.Collaborateur.verifier_token',
    return_value=False
    )

    mock_permissions = mocker.patch(
    'controller.controller.Permissions.verification_persmissions_de_collaborateur',
    return_value=True
    )

    sut = Controller.check_authorization_permission("test_token", "test_role", "test_permission")
    assert mock_token.call_count == 1
    assert mock_permissions.call_count == 0
    assert sut == False


def test_should_return_false_if_collaborateur_has_no_permissions(mocker):
    """Verification de fonctionnment de Controller.check_authorization_permission.
    Doit retourner False si les permissions ne sont pas accordees."""

    mock_token = mocker.patch(
    'controller.controller.Collaborateur.verifier_token',
    return_value=True
    )

    mock_permissions = mocker.patch(
    'controller.controller.Permissions.verification_persmissions_de_collaborateur',
    return_value=False
    )

    sut = Controller.check_authorization_permission("test_token", "test_role", "test_permission")
    assert mock_token.call_count == 1
    assert mock_permissions.call_count == 1
    assert sut == False


def test_should_update_collaborateur_instance(mocker, collaborateur_commercial, role_commercial):
    """Verifie que la fonction Controller.modifier_collaborateur permet de mettre à jour un collaborateur"""

    mock_role = mocker.patch(
            'controller.controller.Role.lister_roles_par_id',
            return_value=[role_commercial]
            ) 


    mock_view = mocker.patch(
        'controller.controller.ViewCollaborateur.modifier_caracteristique',
        side_effect=["y", "y", "y", "y", "y", "n"]
        )

    mock_prenom = mocker.patch(
            'controller.controller.ViewCollaborateur.entrer_prenom_collaborateur',
            return_value="Alan"
            )
    
    mock_nom = mocker.patch(
            'controller.controller.ViewCollaborateur.entrer_nom_collaborateur',
            return_value="Wake"
            )
    
    mock_email = mocker.patch(
            'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
            return_value="aw@gmail.com"
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
    
    mock_hacher_mot_de_pass = mocker.patch('controller.controller.Collaborateur.hacher_mot_de_passe')

    
    mock_valider_session = mocker.patch("controller.controller.valider_session")
    
    Controller.enregistrer_collaborateur(False)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].prenom == "Alan"
    assert mock_valider_session.call_args.args[0].nom == "Wake"
    assert mock_valider_session.call_args.args[0].email == "aw@gmail.com"
    assert mock_valider_session.call_args.args[0].telephone == 555
    assert mock_valider_session.call_args.args[0].mot_de_passe == return_hache


def test_should_remove_collaborateur_from_db(mocker, collaborateur_commercial):
    """Verifie que la fonction Controller.supprimer_collaborateur supprime un collaborateur"""
    mock_valider_session = mocker.patch("controller.controller.valider_sessions_supprimer_objet")
    Controller.supprimer_collaborateur(collaborateur_commercial)
    assert mock_valider_session.call_count == 1