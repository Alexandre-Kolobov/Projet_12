from views.view_client import ViewClient

def test_enter_valide_client_first_name(mocker):
    """Fonctionnement avec un prenom valide ViewClient.entrer_prenom_client"""
    mocker.patch('builtins.input', return_value="Steve")
    sut = ViewClient.entrer_prenom_client()

    assert sut == "Steve"


def test_enter_invalide_collaborateur_first_name(mocker, capsys):
    """Fonctionnement avec un prenom valide ViewClient.entrer_prenom_client"""
    mocker.patch('builtins.input', side_effect=["", "ValideFirstName"])
    ViewClient.entrer_prenom_client()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le prénom du client doit contenir que des lettres et ne pas être vide" in sut

def test_enter_valide_client_name(mocker):
    """Fonctionnement avec un nom valide ViewClient.entrer_nom_client"""
    mocker.patch('builtins.input', return_value="Jobs")
    sut = ViewClient.entrer_nom_client()

    assert sut == "Jobs"


def test_enter_invalide_client_name(mocker, capsys):
    """Fonctionnement avec un nom valide ViewClient.entrer_nom_client"""
    mocker.patch('builtins.input', side_effect=["", "ValideName"])
    ViewClient.entrer_nom_client()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le nom du client doit contenir que des lettres et ne pas être vide" in sut

def test_enter_valide_client_email(mocker):
    """Fonctionnement avec un email valide ViewClient.entrer_email_client"""
    mocker.patch('builtins.input', return_value="sj@gmail.com")
    sut = ViewClient.entrer_email_client()

    assert sut == "sj@gmail.com"


def test_enter_invalide_client_email(mocker, capsys):
    """Fonctionnement avec un email non valide ViewClient.entrer_email_client"""
    mocker.patch('builtins.input', side_effect=["", "ValideEmail"])
    ViewClient.entrer_email_client()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: L'email du client ne doit pas être vide" in sut


def test_enter_valide_client_telephone(mocker):
    """Fonctionnement avec un telephone valide ViewClient.entrer_telephone_client"""
    mocker.patch('builtins.input', return_value="555")
    sut = ViewClient.entrer_telephone_client()

    assert sut == "555"


def test_enter_invalide_client_telephone(mocker, capsys):
    """Fonctionnement avec un telephone non valide ViewClient.entrer_telephone_client"""
    mocker.patch('builtins.input', side_effect=["test", "555"])
    ViewClient.entrer_telephone_client()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: Le numero telephone doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_valide_client_company(mocker):
    """Fonctionnement avec un email valide ViewClient.entrer_entreprise_client"""
    mocker.patch('builtins.input', return_value="Apple")
    sut = ViewClient.entrer_entreprise_client()

    assert sut == "Apple"


def test_enter_invalide_client_company(mocker, capsys):
    """Fonctionnement avec un email non valide ViewClient.entrer_entreprise_client"""
    mocker.patch('builtins.input', side_effect=["", "ValideCompany"])
    ViewClient.entrer_entreprise_client()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Erreur: L'entreprise du collaborateur ne doit pas être vide" in sut


def test_should_retrun_id_to_update_from_user(mocker):
    """Verifier le fonctionnement de ViewClient.demander_id_du_client_a_modifier"""

    mocker.patch('builtins.input', return_value="1")
    sut = ViewClient.demander_id_du_client_a_modifier()

    assert sut == "1"

def test_should_return_true_if_user_want_to_modify_one_more_client(mocker):
    """Verifier que la fonction ViewClient.demander_de_modifier_un_autre_client retourne true"""
    
    mocker.patch('builtins.input', return_value="y")
    sut = ViewClient.demander_de_modifier_un_autre_client()

    assert sut == True


def test_should_retrun_id_to_delete_from_user(mocker):
    """Verifier le fonctionnement de ViewClient.demander_id_du_client_a_supprimer"""

    mocker.patch('builtins.input', return_value="1")
    sut = ViewClient.demander_id_du_client_a_supprimer()

    assert sut == "1"

def test_should_return_true_if_user_want_to_delete_client(mocker, client):
    """Verifier que la fonction ViewClient.demander_de_confirmer_suppression_client retourne true"""
    
    mocker.patch('builtins.input', return_value="y")
    sut = ViewClient.demander_de_confirmer_suppression_client(client)

    assert sut == True


def test_should_return_false_if_user_dont_want_to_delete_client(mocker, client):
    """Verifier que la fonction ViewClient.demander_de_confirmer_suppression_client retourne false"""
    
    mocker.patch('builtins.input', return_value="n")
    sut = ViewClient.demander_de_confirmer_suppression_client(client)

    assert sut == False