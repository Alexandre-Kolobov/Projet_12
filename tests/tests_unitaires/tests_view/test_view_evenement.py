from views.view_evenement import ViewEvenement


def test_enter_valide_start_date(mocker):
    """Verififcation que date de debut de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="10/10/2010 10:00:00")
    sut = ViewEvenement.entrer_date_debut_evenement()

    assert sut == "10/10/2010 10:00:00"


def test_enter_invalide_start_date(mocker, capsys):
    """Verififcation que date de debut de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["Test", "10/10/2010 10:00:00"])
    ViewEvenement.entrer_date_debut_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "does not match format '%d/%m/%Y %H:%M:%S'" in sut


def test_enter_valide_finish_date(mocker):
    """Verififcation que date de debut de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="10/10/2010 10:00:00")
    sut = ViewEvenement.entrer_date_fin_evenement()

    assert sut == "10/10/2010 10:00:00"


def test_enter_invalide_finish_date(mocker, capsys):
    """Verififcation que date de debut de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["Test", "10/10/2010 10:00:00"])
    ViewEvenement.entrer_date_fin_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "does not match format '%d/%m/%Y %H:%M:%S'" in sut


def test_enter_valide_country_name(mocker):
    """Verififcation que le pays de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="France")
    sut = ViewEvenement.entrer_pays_evenement()

    assert sut == "France"


def test_enter_invalide_country_name(mocker, capsys):
    """Verififcation que le pays de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "France"])
    ViewEvenement.entrer_pays_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "Le pays de l'evenement doit contenir que des lettres et ne pas être vide" in sut


def test_enter_valide_city_name(mocker):
    """Verififcation que la ville de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="Paris")
    sut = ViewEvenement.entrer_ville_evenement()

    assert sut == "Paris"


def test_enter_invalide_city_name(mocker, capsys):
    """Verififcation que la ville de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "Paris"])
    ViewEvenement.entrer_ville_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "La ville de l'evenement doit contenir que des lettres et ne pas être vide" in sut


def test_enter_valide_street_name(mocker):
    """Verififcation que la rue de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="RueTest")
    sut = ViewEvenement.entrer_rue_evenement()

    assert sut == "RueTest"


def test_enter_invalide_street_name(mocker, capsys):
    """Verififcation que la rue de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "RueTest"])
    ViewEvenement.entrer_rue_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "La rue de l'evenement doit contenir que des lettres et ne pas être vide" in sut


def test_enter_valide_street_number(mocker):
    """Verififcation que le numero de rue de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="29")
    sut = ViewEvenement.entrer_numero_rue_evenement()

    assert sut == "29"


def test_enter_invalide_street_number(mocker, capsys):
    """Verififcation que le numero de rue de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "29"])
    ViewEvenement.entrer_numero_rue_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "Le numero de rue doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_valide_post_code(mocker):
    """Verififcation que le code postale de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="78000")
    sut = ViewEvenement.entrer_cp_evenement()

    assert sut == "78000"


def test_enter_invalide_post_code(mocker, capsys):
    """Verififcation que le code postale de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "78000"])
    ViewEvenement.entrer_cp_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "Le code postal doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_valide_attendees(mocker):
    """Verififcation que le nombre d'attendees de l'événement est correcte"""
    mocker.patch('builtins.input', return_value="100")
    sut = ViewEvenement.entrer_attendees_evenement()

    assert sut == "100"


def test_enter_invalide_attendees(mocker, capsys):
    """Verififcation que le nombre d'attendees de l'événement est correcte"""
    mocker.patch('builtins.input', side_effect=["", "100"])
    ViewEvenement.entrer_attendees_evenement()

    captured = capsys.readouterr()
    sut = captured.out

    assert "Le nombre d'attendees doit contenir que des chiffres et ne pas être vide" in sut


def test_enter_notes(mocker):
    """Verififcation que les note sont biens prises"""
    mocker.patch('builtins.input', return_value="Test")
    sut = ViewEvenement.entrer_notes_evenement()

    assert sut == "Test"


def test_should_return_id_evenement(mocker, capsys):
    """Demander id du contrat à utilisateur"""
    mocker.patch('builtins.input', return_value="1")
    sut = ViewEvenement.demander_id_de_evenement_a_modifier()

    assert sut == "1"


def test_should_print_that_evenement_doesnt_exists_with_this_id(capsys):
    """Doit dire à l'utilisateur que cet événement n'existe pas"""
    ViewEvenement.evenement_avec_id_nexiste_pas("1")
    captured = capsys.readouterr()
    sut = captured.out

    assert "Evenement avec id" in sut


def test_should_return_collaborateur_id(mocker, collaborateur_support):
    """Verifie fonctionnment ViewEvenement.choisir_collaborateur_id si l'utilisateur choisi un collaborateur de la liste"""
    collaborateur_dict = {
        collaborateur_support.id:
        f"{collaborateur_support.nom} {collaborateur_support.prenom}"
        }
    list_of_dict = [collaborateur_dict]

    mocker.patch('builtins.input', return_value="1")
    sut = ViewEvenement.choisir_collaborateur_id(list_of_dict)

    assert sut is None


def test_should_return_error_when_chose_collaborateur_id(mocker, collaborateur_support, capsys):
    """Verifie fonctionnment ViewContrat.choisir_client_id si l'utilisateur choisi un client de la liste"""
    collaborateur_dict = {collaborateur_support.id: f"{collaborateur_support.nom} {collaborateur_support.prenom}"}
    list_of_dict = [collaborateur_dict]

    mocker.patch('builtins.input', side_effect=["2", "1"])
    ViewEvenement.choisir_collaborateur_id(list_of_dict)
    captured = capsys.readouterr()
    sut = captured.out

    assert "Choissisez le support à assigner pour cet événement:" in sut
