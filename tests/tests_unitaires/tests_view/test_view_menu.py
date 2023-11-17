from views.view_menu import ViewMenu

def test_should_return_user_choice_menu_principal(mocker):
    """Fonctionnement avec un choix valide ViewMenu.afficher_menu_principal"""
    mocker.patch('builtins.input', return_value = "1")
    sut = ViewMenu.afficher_menu_principal()


    assert sut == "COLLABORATEURS"


def test_should_ask_again_about_user_choice_if_choice_is_wrong_menu_principal(mocker, capsys):
    """Fonctionnement avec un choix non valide ViewMenu.afficher_menu_principal"""
    mocker.patch('builtins.input', side_effect=["99", "1"])
    sut = ViewMenu.afficher_menu_principal()

    captured = capsys.readouterr()
    sut = captured.out

    assert "ne correspond pas aux choix proposés" in sut


def test_should_return_user_choice_menu_collaborateur(mocker):
    """Fonctionnement avec un choix valide ViewMenu.afficher_menu_collaborateurs"""
    mocker.patch('builtins.input', return_value = "1")
    sut = ViewMenu.afficher_menu_model("test")


    assert sut == "AFFICHER"


def test_should_ask_again_about_user_choice_if_choice_is_wrong_menu_collaborateur(mocker, capsys):
    """Fonctionnement avec un choix non valide ViewMenu.afficher_menu_collaborateurs"""
    mocker.patch('builtins.input', side_effect=["99", "1"])
    sut = ViewMenu.afficher_menu_model("test")

    captured = capsys.readouterr()
    sut = captured.out

    assert "ne correspond pas aux choix proposés" in sut


def test_should_return_user_choice_menu_filtre_contrat(mocker):
    """Fonctionnement avec un choix valide ViewMenu.afficher_menu_filtre_contrat"""
    mocker.patch('builtins.input', return_value = "1")
    sut = ViewMenu.afficher_menu_filtre_contrat()


    assert sut == "TOUS"


def test_should_ask_again_about_user_choice_if_choice_is_wrong_menu_filtre_contrat(mocker, capsys):
    """Fonctionnement avec un choix non valide ViewMenu.afficher_menu_filtre_contrat"""
    mocker.patch('builtins.input', side_effect=["99", "1"])
    sut = ViewMenu.afficher_menu_filtre_contrat()

    captured = capsys.readouterr()
    sut = captured.out

    assert "ne correspond pas aux choix proposés" in sut


def test_should_return_user_choice_menu_filtre_evenement(mocker):
    """Fonctionnement avec un choix valide ViewMenu.afficher_menu_filtre_evenement"""
    mocker.patch('builtins.input', return_value = "1")
    sut = ViewMenu.afficher_menu_filtre_evenement()


    assert sut == "TOUS"


def test_should_ask_again_about_user_choice_if_choice_is_wrong_menu_filtre_evenement(mocker, capsys):
    """Fonctionnement avec un choix non valide ViewMenu.afficher_menu_filtre_evenement"""
    mocker.patch('builtins.input', side_effect=["99", "1"])
    sut = ViewMenu.afficher_menu_filtre_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "ne correspond pas aux choix proposés" in sut