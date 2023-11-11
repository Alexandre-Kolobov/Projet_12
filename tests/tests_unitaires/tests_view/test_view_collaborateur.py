from views.view_collaborateur import ViewCollaborateur

def test_should_print_initialisation_collaborateur(capsys):
    """Verifier le texte d'initialisation de collaborateur ViewCollaborateur.initialisation_collaborateur"""
    ViewCollaborateur.initialisation_collaborateur()
    captured = capsys.readouterr()
    sut_1 = "----------------------------------------"
    sut_2 = "Pour le premiere lancement de l'application nous devons créer un utilisateur gestionnaire."

    assert sut_1 in captured.out
    assert sut_2 in captured.out

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


def test_enter_valide_collaborateur_email(mocker):
    """Fonctionnement avec un telephone valide ViewCollaborateur.entrer_telephone_collaborateur"""
    mocker.patch('builtins.input', return_value="555")
    sut = ViewCollaborateur.entrer_telephone_collaborateur()

    assert sut == "555"


def test_enter_invalide_collaborateur_email(mocker, capsys):
    """Fonctionnement avec un telephone non valide ViewCollaborateur.entrer_telephone_collaborateur"""
    mocker.patch('builtins.input', side_effect=["test", "555"])
    ViewCollaborateur.entrer_telephone_collaborateur()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le numero telephone doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_valide_collaborateur_password(mocker):
    """Fonctionnement avec un mot de passe valide ViewCollaborateur.entrer_mot_de_passe_collaborateur"""
    mocker.patch('builtins.input', return_value="test01")
    sut = ViewCollaborateur.entrer_mot_de_passe_collaborateur()

    assert sut == "test01"


def test_enter_invalide_collaborateur_password(mocker, capsys):
    """Fonctionnement avec un mot de passe non valide ViewCollaborateur.entrer_mot_de_passe_collaborateur"""
    mocker.patch('builtins.input', side_effect=["", "test01"])
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

    