from views.view_collaborateur import ViewCollaborateur

def test_should_print_initialisation_collaborateur(capsys):
    """Verifier le texte d'initialisation de collaborateur ViewCollaborateur.initialisation_collaborateur"""
    ViewCollaborateur.initialisation_collaborateur()
    captured = capsys.readouterr()
    sut_1 = "----------------------------------------"
    sut_2 = "Pour le premiere lancement de l'application nous devons créer un utilisateur gestionnaire."

    assert sut_1 in captured.out
    assert sut_2 in captured.out.strip()

def test_enter_valide_collaborateur_first_name(mocker):
    """Fonctionnement avec un prenom valide ViewCollaborateur.entrer_prenom_collaborateur"""
    mocker.patch('builtins.input', return_value="Steve")
    sut = ViewCollaborateur.entrer_prenom_collaborateur()

    assert sut == "Steve"


def test_enter_invalide_collaborateur_first_name(mocker, capsys):
    """Fonctionnement avec un prenom valide ViewCollaborateur.entrer_prenom_collaborateur"""
    mocker.patch('builtins.input', side_effect=["", "ValideFirstName"])
    ViewCollaborateur.entrer_prenom_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le prénom du collaborateur doit contenir que des lettres et ne pas être vide" in sut


def test_enter_valide_collaborateur_name(mocker):
    """Fonctionnement avec un nom valide ViewCollaborateur.entrer_nom_collaborateur"""
    mocker.patch('builtins.input', return_value="Jobs")
    sut = ViewCollaborateur.entrer_nom_collaborateur()

    assert sut == "Jobs"


def test_enter_invalide_collaborateur_name(mocker, capsys):
    """Fonctionnement avec un nom valide ViewCollaborateur.entrer_nom_collaborateur"""
    mocker.patch('builtins.input', side_effect=["", "ValideName"])
    ViewCollaborateur.entrer_nom_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le nom du collaborateur doit contenir que des lettres et ne pas être vide" in sut


def test_enter_valide_collaborateur_email(mocker):
    """Fonctionnement avec un email valide ViewCollaborateur.entrer_email_collaborateur"""
    mocker.patch('builtins.input', return_value="sj@gmail.com")
    sut = ViewCollaborateur.entrer_email_collaborateur()

    assert sut == "sj@gmail.com"


def test_enter_invalide_collaborateur_email(mocker, capsys):
    """Fonctionnement avec un email non valide ViewCollaborateur.entrer_email_collaborateur"""
    mocker.patch('builtins.input', side_effect=["", "ValideEmail"])
    ViewCollaborateur.entrer_email_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: L'email du collaborateur ne doit pas être vide" in sut


def test_enter_valide_collaborateur_telephone(mocker):
    """Fonctionnement avec un telephone valide ViewCollaborateur.entrer_telephone_collaborateur"""
    mocker.patch('builtins.input', return_value="555")
    sut = ViewCollaborateur.entrer_telephone_collaborateur()

    assert sut == "555"


def test_enter_invalide_collaborateur_telephone(mocker, capsys):
    """Fonctionnement avec un telephone non valide ViewCollaborateur.entrer_telephone_collaborateur"""
    mocker.patch('builtins.input', side_effect=["test", "555"])
    ViewCollaborateur.entrer_telephone_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le numero telephone doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_valide_collaborateur_password(mocker):
    """Fonctionnement avec un mot de passe valide ViewCollaborateur.entrer_mot_de_passe_collaborateur"""
    mocker.patch('getpass.getpass', return_value="test01")
    sut = ViewCollaborateur.entrer_mot_de_passe_collaborateur()

    assert sut == "test01"


def test_enter_invalide_collaborateur_password(mocker, capsys):
    """Fonctionnement avec un mot de passe non valide ViewCollaborateur.entrer_mot_de_passe_collaborateur"""
    mocker.patch('getpass.getpass', side_effect=["", "test01"])
    ViewCollaborateur.entrer_mot_de_passe_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le mot de passe ne doit pas être vide" in sut


def test_valide_choice_of_role(mocker):
    """Fonctionnement avec un choix valide ViewCollaborateur.choisir_role_collaborateur"""
    roles_as_list_of_dict = ({1:"gestion"}, {2:"commerciale"}, {3:"support"})
    mocker.patch('builtins.input', return_value="1")
    sut = ViewCollaborateur.choisir_role_collaborateur(roles_as_list_of_dict)

    assert sut == 1


def test_invalide_choice_of_role(mocker,capsys):
    """Fonctionnement avec un choix invalide ViewCollaborateur.choisir_role_collaborateur"""
    roles_as_list_of_dict = ({1:"gestion"}, {2:"commerciale"}, {3:"support"})
    mocker.patch('builtins.input', side_effect=["4", "1"])
    ViewCollaborateur.choisir_role_collaborateur(roles_as_list_of_dict)

    captured = capsys.readouterr()
    sut = captured.out

    assert "Merci de choisir parmis les roles proposés" in sut


def test_should_print_wrong_authentication(capsys):
    """Verifier le texte de refus d'authentification est correcte ViewCollaborateur.refuser_authentification"""
    ViewCollaborateur.refuser_authentification()
    captured = capsys.readouterr()
    sut_1 = "----------------------------------------"
    sut_2 = "Les informations d'identification ne sont pas correctes"
    sut_3 = "Merci de reesayer"

    assert sut_1 in captured.out
    assert sut_2 in captured.out
    assert sut_3 in captured.out


def test_should_print_token_fails(capsys):
    """Verifier le texte pour un token erroné ViewCollaborateur.refuser_token"""
    ViewCollaborateur.refuser_token()
    captured = capsys.readouterr()
    sut = "Le token n'est pas correcte"

    assert sut in captured.out


def test_should_print_permissions_fails(capsys):
    """Verifier le texte pour un token erroné ViewCollaborateur.refuser_permissions"""
    ViewCollaborateur.refuser_permissions()
    captured = capsys.readouterr()
    sut = "Vous n'avez pas de permission pour réaliser cette action"

    assert sut in captured.out


def test_should_confirm_that_collaborateur_was_added(capsys, collaborateur_gestionnaire):
    """Verifier le texte pour enregistrement d'un collaborateur est ok ViewCollaborateur.confirmation_ajout_collaborateur"""
    ViewCollaborateur.confirmation_ajout_collaborateur(collaborateur_gestionnaire)
    captured = capsys.readouterr()
    sut = f"Le collaborateur {collaborateur_gestionnaire.nom} {collaborateur_gestionnaire.prenom} a été ajouté"

    assert sut in captured.out


def test_should_return_true_if_user_want_to_add_one_more_collaborateur(mocker):
    """Verifier que la fonction ViewCollaborateur.redemander_ajouter_collaborateur retourne true"""
    
    mocker.patch('builtins.input', return_value="y")
    sut = ViewCollaborateur.redemander_ajouter_collaborateur()

    assert sut == True


def test_should_return_false_if_user_dont_want_to_add_one_more_collaborateur(mocker):
    """Verifier que la fonction ViewCollaborateur.redemander_ajouter_collaborateur retourne true"""
    
    mocker.patch('builtins.input', return_value="n")
    sut = ViewCollaborateur.redemander_ajouter_collaborateur()

    assert sut == False

def test_should_print_message_about_authentication(capsys):
    """Verifier le fonctionnement de ViewCollaborateur.demander_authentification"""
    ViewCollaborateur.demander_authentification()
    captured = capsys.readouterr()
    sut = "Entrer votre email et mot de passe pour se connecter"

    assert sut in captured.out

def test_should_retrun_id_to_update_from_user(mocker):
    """Verifier le fonctionnement de ViewCollaborateur.demander_id_du_collaborateur_a_modifier"""

    mocker.patch('builtins.input', return_value="1")
    sut = ViewCollaborateur.demander_id_du_collaborateur_a_modifier()

    assert sut == "1"


def test_should_retrun_id_to_delete_from_user(mocker):
    """Verifier le fonctionnement de ViewCollaborateur.demander_id_du_collaborateur_a_supprimer"""

    mocker.patch('builtins.input', return_value="1")
    sut = ViewCollaborateur.demander_id_du_collaborateur_a_supprimer()

    assert sut == "1"


def test_should_return_true_if_user_want_to_modify_one_more_collaborateur(mocker):
    """Verifier que la fonction ViewCollaborateur.demander_de_modifier_un_autre_collaborateur retourne true"""
    
    mocker.patch('builtins.input', return_value="y")
    sut = ViewCollaborateur.demander_de_modifier_un_autre_collaborateur()

    assert sut == True


def test_should_return_false_if_user_dont_want_to_modify_one_more_collaborateur(mocker):
    """Verifier que la fonction ViewCollaborateur.demander_de_modifier_un_autre_collaborateur retourne false"""
    
    mocker.patch('builtins.input', return_value="n")
    sut = ViewCollaborateur.demander_de_modifier_un_autre_collaborateur()

    assert sut == False


def test_should_return_true_if_user_want_to_delete_collaborateur(mocker, collaborateur_gestionnaire):
    """Verifier que la fonction ViewCollaborateur.demander_de_confirmer_suppression_collaborateur retourne true"""
    
    mocker.patch('builtins.input', return_value="y")
    sut = ViewCollaborateur.demander_de_confirmer_suppression_collaborateur(collaborateur_gestionnaire)

    assert sut == True


def test_should_return_false_if_user_dont_want_to_delete_collaborateur(mocker, collaborateur_gestionnaire):
    """Verifier que la fonction ViewCollaborateur.demander_de_confirmer_suppression_collaborateur retourne false"""
    
    mocker.patch('builtins.input', return_value="n")
    sut = ViewCollaborateur.demander_de_confirmer_suppression_collaborateur(collaborateur_gestionnaire)

    assert sut == False