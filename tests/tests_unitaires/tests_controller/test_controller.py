from controller.controller import Controller
from permissions.permissions_manager import Permissions
from models.role import Role
import bcrypt


def test_should_return_true_if_list_non_vide(mocker):
    """Verifie que la fonction Controller.roles_existent_dans_db retourn true si roles existent"""
    mock = mocker.patch('controller.controller.Role.lister_roles', return_value=[1, 2, 3])
    sut = Controller.roles_existent_dans_db()

    assert mock.call_count == 1
    assert sut is True


def test_should_return_false_if_list_vide(mocker):
    """Verifie que la fonction Controller.roles_existent_dans_db retourn false si roles n'existent pas"""
    mock = mocker.patch('controller.controller.Role.lister_roles', return_value=[])
    sut = Controller.roles_existent_dans_db()

    assert mock.call_count == 1
    assert sut is False


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
    assert sut is True


def test_should_return_false_if_collaborateur_doesnt_exist_in_db(mocker):
    """Verifie que la fonction Controller.collaborateurs_existent_dans_db fait return bool correctement"""
    mock = mocker.patch('controller.controller.Collaborateur.lister_collaborateurs', return_value=[])

    sut = Controller.collaborateurs_existent_dans_db()
    assert mock.call_count == 1
    assert sut is False


def test_should_create_collaborateur_instance_if_first_user_doesnt_exists(mocker):
    """Verifie que la fonction Controller.enregistrer_collaborateur enregistre premiere collaborateur comme gestionnaire"""

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_prenom_collaborateur',
        return_value="Steve"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_nom_collaborateur',
        return_value="Jobs"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
        return_value="sj@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_telephone_collaborateur',
        return_value=555
        )

    mot_de_pass = "123456"
    return_hache = bcrypt.hashpw(mot_de_pass.encode('utf-8'), bcrypt.gensalt())

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value=return_hache
        )

    role_gestionnaire = Role(id=1, role_name="gestion")
    role_commercial = Role(id=2, role_name="commercial")
    role_support = Role(id=3, role_name="support")

    mocker.patch(
        'controller.controller.Role.lister_roles',
        return_value=[role_gestionnaire, role_commercial, role_support]
        )

    mocker.patch(
        'controller.controller.Role.lister_roles_par_nom',
        return_value=[role_gestionnaire]
        )

    mocker.patch('controller.controller.Collaborateur.hacher_mot_de_passe')

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

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
        return_value="test_fails@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value="password_fails"
        )

    mocker.patch(
        'controller.controller.Collaborateur.selectionner_collaborateurs_par_email',
        return_value=[]
        )

    mock_refuser_authentification = mocker.patch('controller.controller.ViewCollaborateur.refuser_authentification')

    sut = Controller.authentication_user()
    assert mock_refuser_authentification.call_count == 1
    assert sut is None


def test_should_return_none_if_wrong_password_when_authetication(mocker, collaborateur_gestionnaire):
    """Verification de fonctionnment de Controller.authentication_user.
    Doit retourner None si authentification echou et appeler ViewCollaborateur.refuser_authentification.
    Dans ce cas l'authentification doit echouer car le mot de pass ne correspond pas à celui associé au login."""

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
        return_value="test_fails@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value="password_fails"
        )

    mocker.patch(
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
    assert sut is None


def test_should_return_collaborateur_if_credentials_are_ok(mocker, collaborateur_gestionnaire):
    """Verification de fonctionnment de Controller.authentication_user.
    Doit retourner collaborateur si authentification est ok."""

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
        return_value="ae@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value="123456"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value="password_fails"
        )

    mocker.patch(
        'controller.controller.Collaborateur.selectionner_collaborateurs_par_email',
        return_value=[collaborateur_gestionnaire]
        )

    mocker.patch(
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
    assert sut is True


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
    assert sut is False


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
    assert sut is False


def test_should_update_collaborateur_instance(mocker, collaborateur_commercial, role_commercial):
    """Verifie que la fonction Controller.modifier_collaborateur permet de mettre à jour un collaborateur"""

    mocker.patch(
        'controller.controller.Role.lister_roles_par_id',
        return_value=[role_commercial]
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.modifier_caracteristique',
        side_effect=[True, True, True, True, True, True]
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_prenom_collaborateur',
        return_value="Alan"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_nom_collaborateur',
        return_value="Wake"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_email_collaborateur',
        return_value="aw@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_telephone_collaborateur',
        return_value=555
        )

    mocker.patch('controller.controller.Role.lister_roles')

    mocker.patch(
        'controller.controller.ViewCollaborateur.choisir_role_collaborateur',
        return_value=None
        )

    mot_de_pass = "123456"
    return_hache = bcrypt.hashpw(mot_de_pass.encode('utf-8'), bcrypt.gensalt())

    mocker.patch(
        'controller.controller.ViewCollaborateur.entrer_mot_de_passe_collaborateur',
        return_value=return_hache
        )

    mocker.patch('controller.controller.Collaborateur.hacher_mot_de_passe')

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.modifier_collaborateur(collaborateur_commercial)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].prenom == "Alan"
    assert mock_valider_session.call_args.args[0].nom == "Wake"
    assert mock_valider_session.call_args.args[0].email == "aw@gmail.com"
    assert mock_valider_session.call_args.args[0].telephone == 555
    assert mock_valider_session.call_args.args[0].mot_de_passe == return_hache
    assert mock_valider_session.call_args.args[0].role is None


def test_should_remove_collaborateur_from_db(mocker, collaborateur_commercial):
    """Verifie que la fonction Controller.supprimer_obj supprime un collaborateur"""
    mock_valider_session = mocker.patch("controller.controller.valider_sessions_supprimer_objet")
    Controller.supprimer_obj(collaborateur_commercial)
    assert mock_valider_session.call_count == 1


def test_should_create_client_instance(mocker):
    """Verifie que la fonction Controller.enregistrer_client enregistre un client"""

    mocker.patch(
        'controller.controller.ViewClient.entrer_nom_client',
        return_value="Jobs"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_prenom_client',
        return_value="Steve"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_email_client',
        return_value="sj@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_telephone_client',
        return_value=555
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_entreprise_client',
        return_value="Apple"
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.enregistrer_client(3)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].prenom == "Steve"
    assert mock_valider_session.call_args.args[0].nom == "Jobs"
    assert mock_valider_session.call_args.args[0].email == "sj@gmail.com"
    assert mock_valider_session.call_args.args[0].telephone == 555
    assert mock_valider_session.call_args.args[0].entreprise == "Apple"
    assert mock_valider_session.call_args.args[0].collaborateur_id == 3


def test_should_update_client_instance(mocker, client):
    """Verifie que la fonction Controller.modifier_client permet de mettre à jour un client"""

    mocker.patch(
        'controller.controller.ViewClient.modifier_caracteristique',
        side_effect=[True, True, True, True, True]
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_nom_client',
        return_value="TestNom"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_prenom_client',
        return_value="TestPrenom"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_email_client',
        return_value="test@gmail.com"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_telephone_client',
        return_value="101415"
        )

    mocker.patch(
        'controller.controller.ViewClient.entrer_entreprise_client',
        return_value="TestEntreprise"
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.modifier_client(client)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].nom == "TestNom"
    assert mock_valider_session.call_args.args[0].prenom == "TestPrenom"
    assert mock_valider_session.call_args.args[0].email == "test@gmail.com"
    assert mock_valider_session.call_args.args[0].telephone == "101415"
    assert mock_valider_session.call_args.args[0].entreprise == "TestEntreprise"


def test_should_return_true_if_ids_are_the_same():
    """Verification de l'égalité des id pour fonction Controller.check_exclusive_permission"""
    sut = Controller.check_exclusive_permission(1, 1)
    assert sut is True


def test_should_return_false_if_ids_are_not_the_same():
    """Verification de l'égalité des id pour fonction Controller.check_exclusive_permission"""
    sut = Controller.check_exclusive_permission(2, 1)
    assert sut is False


def test_should_create_contrat_instance(mocker, collaborateur_commercial):
    """Verifie que la fonction Controller.enregistrer_contrat enregistre un contrat"""

    mocker.patch(
        'controller.controller.ViewContrat.entrer_montant_total',
        return_value=100
        )

    mocker.patch(
        'controller.controller.ViewContrat.entrer_reste_a_payer',
        return_value=50
        )

    mocker.patch(
        'controller.controller.ViewContrat.choisir_statut',
        return_value=True
        )

    mocker.patch(
        'controller.controller.ViewContrat.choisir_client_id',
        return_value=1
        )

    mocker.patch(
        'controller.controller.Collaborateur.selectionner_collaborateurs_par_client_id',
        return_value=[collaborateur_commercial]
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.enregistrer_contrat()
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].montant_total == 100
    assert mock_valider_session.call_args.args[0].reste_a_payer == 50
    assert mock_valider_session.call_args.args[0].statut_signe is True
    assert mock_valider_session.call_args.args[0].client_id == 1
    assert mock_valider_session.call_args.args[0].collaborateur_id == collaborateur_commercial.id


def test_should_update_contrat_instance(mocker, contrat):
    """Verifie que la fonction Controller.modifier_contrat permet de mettre à jour un client"""

    mocker.patch(
        'controller.controller.ViewContrat.modifier_caracteristique',
        side_effect=[True, True, True]
        )

    mocker.patch(
            'controller.controller.ViewContrat.entrer_montant_total',
            return_value="100"
            )

    mocker.patch(
            'controller.controller.ViewContrat.entrer_reste_a_payer',
            return_value="0"
            )

    mocker.patch(
            'controller.controller.ViewContrat.choisir_statut',
            return_value=False
            )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.modifier_contrat(contrat)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].montant_total == "100"
    assert mock_valider_session.call_args.args[0].reste_a_payer == "0"
    assert mock_valider_session.call_args.args[0].statut_signe is False


def test_should_create_evenement_instance(mocker, contrat):
    """Verifie que la fonction Controller.enregistrer_contrat enregistre un contrat"""

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_debut_evenement',
        return_value="10/10/2020 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_fin_evenement',
        return_value="10/10/2021 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_pays_evenement',
        return_value="France"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_ville_evenement',
        return_value="Paris"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_rue_evenement',
        return_value="RueTest"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_numero_rue_evenement',
        return_value="10"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_cp_evenement',
        return_value="78000"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_attendees_evenement',
        return_value="100"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_notes_evenement',
        return_value="Test notes"
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.enregistrer_evenement(contrat)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].date_debut == "10/10/2020 14:00:00"
    assert mock_valider_session.call_args.args[0].date_fin == "10/10/2021 14:00:00"
    assert mock_valider_session.call_args.args[0].location_pays == "France"
    assert mock_valider_session.call_args.args[0].location_ville == "Paris"
    assert mock_valider_session.call_args.args[0].location_rue == "RueTest"
    assert mock_valider_session.call_args.args[0].location_num_rue == "10"
    assert mock_valider_session.call_args.args[0].location_cp == "78000"
    assert mock_valider_session.call_args.args[0].attendees == "100"
    assert mock_valider_session.call_args.args[0].notes == "Test notes"


def test_should_update_evenement_instance_gestion(mocker, evenement):
    """Verifie que la fonction Controller.modifier_evenement_gestion
    permet de mettre à jour un evenement pour un utilisateur gestion"""

    mocker.patch(
        'controller.controller.ViewEvenement.modifier_caracteristique',
        side_effect=[True, True, True, True, True, True, True, True, True, False]
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_debut_evenement',
        return_value="15/10/2020 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_fin_evenement',
        return_value="16/10/2020 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_pays_evenement',
        return_value="Russie"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_ville_evenement',
        return_value="Moscow"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_rue_evenement',
        return_value="RueTest"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_numero_rue_evenement',
        return_value="26"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_cp_evenement',
        return_value="06000"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_attendees_evenement',
        return_value="100"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_notes_evenement',
        return_value="Toto"
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.modifier_evenement_gestion(evenement)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].date_debut == "15/10/2020 14:00:00"
    assert mock_valider_session.call_args.args[0].date_fin == "16/10/2020 14:00:00"
    assert mock_valider_session.call_args.args[0].location_pays == "Russie"
    assert mock_valider_session.call_args.args[0].location_ville == "Moscow"
    assert mock_valider_session.call_args.args[0].location_rue == "RueTest"
    assert mock_valider_session.call_args.args[0].location_num_rue == "26"
    assert mock_valider_session.call_args.args[0].location_cp == "06000"
    assert mock_valider_session.call_args.args[0].attendees == "100"
    assert mock_valider_session.call_args.args[0].notes == "Toto"


def test_should_update_evenement_instance_support(mocker, evenement):
    """Verifie que la fonction Controller.modifier_evenement_support
    permet de mettre à jour un evenement pour un utilisateur support"""

    mocker.patch(
        'controller.controller.ViewEvenement.modifier_caracteristique',
        side_effect=[True, True, True, True, True, True, True, True, True, False]
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_debut_evenement',
        return_value="15/10/2020 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_date_fin_evenement',
        return_value="16/10/2020 14:00:00"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_pays_evenement',
        return_value="Russie"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_ville_evenement',
        return_value="Moscow"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_rue_evenement',
        return_value="RueTest"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_numero_rue_evenement',
        return_value="26"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_cp_evenement',
        return_value="06000"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_attendees_evenement',
        return_value="100"
        )

    mocker.patch(
        'controller.controller.ViewEvenement.entrer_notes_evenement',
        return_value="Toto"
        )

    mock_valider_session = mocker.patch("controller.controller.valider_session")

    Controller.modifier_evenement_support(evenement)
    assert mock_valider_session.call_count == 1
    assert mock_valider_session.call_args.args[0].date_debut == "15/10/2020 14:00:00"
    assert mock_valider_session.call_args.args[0].date_fin == "16/10/2020 14:00:00"
    assert mock_valider_session.call_args.args[0].location_pays == "Russie"
    assert mock_valider_session.call_args.args[0].location_ville == "Moscow"
    assert mock_valider_session.call_args.args[0].location_rue == "RueTest"
    assert mock_valider_session.call_args.args[0].location_num_rue == "26"
    assert mock_valider_session.call_args.args[0].location_cp == "06000"
    assert mock_valider_session.call_args.args[0].attendees == "100"
    assert mock_valider_session.call_args.args[0].notes == "Toto"
