from controller.controller import Controller
from io import StringIO
import pytest

def test_function_run_as_gestionnaire(mocker, capsys):
    mocker.patch('builtins.input', side_effect=[
        "ak@gmail.com",
        "1",
        "1",
        "y",
        "5",
        "2",
        "1",
        "y",
        "5",
        "3",
        "5",
        "4",
        "1",
        "3",
        "5",
        "5"
        ]
        )
    mocker.patch('getpass.getpass',  return_value="667745")
    
    with pytest.raises(SystemExit):
        Controller.run()

    ocaptured_output = capsys.readouterr()

    assert "1 - Collaborateurs" in ocaptured_output.out
    assert "2 - Clients" in ocaptured_output.out
    assert "3 - Contrats" in ocaptured_output.out
    assert "4 - Evenements" in ocaptured_output.out
    assert "5 - Quitter" in ocaptured_output.out

    assert "1 - Afficher collaborateurs" in ocaptured_output.out
    assert "2 - Ajouter collaborateur" in ocaptured_output.out
    assert "3 - Modifier collaborateur" in ocaptured_output.out
    assert "4 - Supprimer collaborateur" in ocaptured_output.out
    assert "5 - Revenir dans le menu principal" in ocaptured_output.out
    assert "6 - Quitter" in ocaptured_output.out

    assert "1 - Afficher clients" in ocaptured_output.out
    assert "2 - Ajouter client" in ocaptured_output.out
    assert "3 - Modifier client" in ocaptured_output.out
    assert "4 - Supprimer client" in ocaptured_output.out
    assert "5 - Revenir dans le menu principal" in ocaptured_output.out
    assert "6 - Quitter" in ocaptured_output.out

    assert "1 - Afficher contrats" in ocaptured_output.out
    assert "2 - Ajouter contrat" in ocaptured_output.out
    assert "3 - Modifier contrat" in ocaptured_output.out
    assert "4 - Supprimer contrat" in ocaptured_output.out
    assert "5 - Revenir dans le menu principal" in ocaptured_output.out
    assert "6 - Quitter" in ocaptured_output.out

    assert "1 - Afficher evenements" in ocaptured_output.out
    assert "2 - Ajouter evenement" in ocaptured_output.out
    assert "3 - Modifier evenement" in ocaptured_output.out
    assert "4 - Supprimer evenement" in ocaptured_output.out
    assert "5 - Revenir dans le menu principal" in ocaptured_output.out
    assert "6 - Quitter" in ocaptured_output.out

    assert "1 - Afficher tous les événements" in ocaptured_output.out
    assert "2 - Afficher les événements sans support" in ocaptured_output.out
    assert "3 - Revenir dans le menu principal" in ocaptured_output.out
    assert "4 - Quitter" in ocaptured_output.out



