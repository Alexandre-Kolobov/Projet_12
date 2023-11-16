from views.view_contrat import ViewContrat

def test_enter_valide_amount(mocker):
    """Fonctionnement avec un montant valide ViewContrat.entrer_montant_total"""
    mocker.patch('builtins.input', return_value="100")
    sut = ViewContrat.entrer_montant_total()

    assert sut == "100"

def test_enter_invalide_amount(mocker, capsys):
    """Fonctionnement avec un montant invalide ViewContrat.entrer_montant_total"""
    mocker.patch('builtins.input', side_effect=["Test", "100"])
    ViewContrat.entrer_montant_total()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Le montant du contrat doit être numerique et ne pas être vide" in sut


def test_enter_valide_due_amount(mocker):
    """Fonctionnement avec un montant valide ViewContrat.entrer_reste_a_payer"""
    mocker.patch('builtins.input', return_value="50")
    sut = ViewContrat.entrer_reste_a_payer("100")

    assert sut == "50"

def test_enter_invalide_due_amount(mocker, capsys):
    """Fonctionnement avec un montant invalide ViewContrat.entrer_reste_a_payer"""
    mocker.patch('builtins.input', side_effect=["Test", "10"])
    ViewContrat.entrer_reste_a_payer("100")
    captured = capsys.readouterr()
    sut = captured.out

    assert "Le reste a payer du contrat doit être numerique et ne pas être vide et être inférieur au montant total" in sut

def test_enter_too_big_due_amount(mocker, capsys):
    """Fonctionnement avec un montant superieur à montant total ViewContrat.entrer_reste_a_payer"""
    mocker.patch('builtins.input', side_effect=["1000","10"])
    ViewContrat.entrer_reste_a_payer("100")
    captured = capsys.readouterr()
    sut = captured.out

    assert "Le reste a payer du contrat doit être numerique et ne pas être vide et être inférieur au montant total" in sut

def test_should_retourn_true_if_contrat_is_signed(mocker):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi y"""
    mocker.patch('builtins.input', return_value="y")
    sut = ViewContrat.choisir_statut()
    assert sut == True

def test_should_retourn_false_if_contrat_is_not_signed(mocker):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi n"""
    mocker.patch('builtins.input', return_value="n")
    sut = ViewContrat.choisir_statut()
    assert sut == False

def test_should_retourn_error_if_user_doesnt_chose_yes_or_no(mocker, capsys):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi autre choses que y ou n"""
    mocker.patch('builtins.input', side_effect=["test","y"])
    ViewContrat.choisir_statut()
    captured = capsys.readouterr()
    sut = captured.out
    assert "Merci d'utiliser y or n" in sut