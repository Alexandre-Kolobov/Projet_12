from models.client import Client

def test_should_return_list_of_clients(mocker):
    """La fonction doit retourner une liste des clients Client.lister_clients
    en applant fonction ClientQueries.lister_clients_dao"""

    mock = mocker.patch('models.client.ClientQueries.lister_clients_dao')

    sut = Client.lister_clients()

    mock.assert_called_once_with(Client) # si ne retourne pas AssertionError c'est ok 
    assert mock.call_count == 1  # Pour confirmer appel au mock