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
    mocker.patch('builtins.input', side_effect=["1000", "10"])
    ViewContrat.entrer_reste_a_payer("100")
    captured = capsys.readouterr()
    sut = captured.out

    assert "Le reste a payer du contrat doit être numerique et ne pas être vide et être inférieur au montant total" in sut


def test_should_return_true_if_contrat_is_signed(mocker):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi y"""
    mocker.patch('builtins.input', return_value="y")
    sut = ViewContrat.choisir_statut()
    assert sut is True


def test_should_return_false_if_contrat_is_not_signed(mocker):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi n"""
    mocker.patch('builtins.input', return_value="n")
    sut = ViewContrat.choisir_statut()
    assert sut is False


def test_should_return_error_if_user_doesnt_chose_yes_or_no(mocker, capsys):
    """Verifie fonctionnment ViewContrat.choisir_statut si l'utilisateur choisi autre choses que y ou n"""
    mocker.patch('builtins.input', side_effect=["test", "y"])
    ViewContrat.choisir_statut()
    captured = capsys.readouterr()
    sut = captured.out
    assert "Merci d'utiliser y or n" in sut


def test_should_return_client_id(mocker, client):
    """Verifie fonctionnment ViewContrat.choisir_client_id si l'utilisateur choisi un client de la liste"""
    client_dict = {client.id: f"{client.nom} {client.prenom} - {client.entreprise}"}
    list_of_dict = [client_dict]

    mocker.patch('builtins.input', return_value="1")
    sut = ViewContrat.choisir_client_id(list_of_dict)

    assert sut is None  # id du client est None car pas de connexion vers DB


def test_should_return_error_when_chose_client_id(mocker, client, capsys):
    """Verifie fonctionnment ViewContrat.choisir_client_id si l'utilisateur ne choisi pas un client de la liste"""
    client_dict = {client.id: f"{client.nom} {client.prenom} - {client.entreprise}"}
    list_of_dict = [client_dict]

    mocker.patch('builtins.input', side_effect=["2", "1"])

    ViewContrat.choisir_client_id(list_of_dict)
    captured = capsys.readouterr()
    sut = captured.out

    assert "Merci de choisir parmis les clients proposés" in sut


def test_should_return_error_when_chose_collaborateur_id(mocker, collaborateur_commercial, capsys):
    """Verifie fonctionnment ViewContrat.choisir_client_id si l'utilisateur choisi un client de la liste"""
    collaborateur_dict = {collaborateur_commercial.id: f"{collaborateur_commercial.nom} {collaborateur_commercial.prenom}"}
    list_of_dict = [collaborateur_dict]

    mocker.patch('builtins.input', side_effect=["2", "1"])
    ViewContrat.choisir_collaborateur_id(list_of_dict)
    captured = capsys.readouterr()
    sut = captured.out

    assert "Merci de choisir parmis les collaborateurs proposés" in sut


def test_should_return_contrat_id_to_modify(mocker):
    """Verifie fonctionnment ViewContrat.demander_id_du_contrat_a_modifier return m'id du contrat """
    mocker.patch('builtins.input', return_value="2")
    sut = ViewContrat.demander_id_du_contrat_a_modifier()

    assert sut == "2"


def test_should_return_id_contrat(mocker, capsys):
    """Demander id du contrat à utilisateur"""
    mocker.patch('builtins.input', return_value="1")
    sut = ViewContrat.demander_id_du_contrat_pour_evenement()

    assert sut == "1"


def test_should_return_error_if_id_contrat_is_wrong_type(mocker, capsys):
    """Demander id du contrat à utilisateur"""
    mocker.patch('builtins.input', side_effect=["abc", "1"])
    ViewContrat.demander_id_du_contrat_pour_evenement()
    captured = capsys.readouterr()
    sut = captured.out

    assert "L'id du contrat doit être numerique et ne pas être vide" in sut


def test_should_return_error_if_contrat_no_signed(capsys):
    """Demander id du contrat à utilisateur"""
    ViewContrat.contrat_avec_id_nest_pas_signe()
    captured = capsys.readouterr()
    sut = captured.out

    assert "Ce contrat n'est pas signé. Impossible de créer un événement." in sut
