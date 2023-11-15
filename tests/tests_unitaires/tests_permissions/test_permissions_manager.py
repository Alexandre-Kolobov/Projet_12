from permissions.permissions_manager import Permissions

@staticmethod
def test_should_retourn_true_for_permissions():
    """Permet de tester un cas de permissions accordées"""
    sut = Permissions.verification_persmissions_de_collaborateur("gestion", "lecture_collaborateurs")
    assert sut == True

def test_should_retourn_false_for_permissions():
    """Permet de tester un cas de permissions non accordées"""
    sut = Permissions.verification_persmissions_de_collaborateur("commercial", "supprimer_collaborateur")
    assert sut == False