import requests


def auth(facility, token):
    """
    This method verifies that the User who wants to publish a news is an admin at the facility, he want to publish it at.
    It verifies it with interrogating the ELIXIR AAI with the Bearer authentication token.
    :param facility: facility id which should be verified
    :param token: Bearer authentication token
    :return:
    """

    hed = {'Authorization': 'Bearer ' + token}
    data = {'facility': facility}
    url = 'https://perun.elixir-czech.cz/oauth/rpc/json/authzResolver/isFacilityAdmin'
    response = requests.post(url, json=data, headers=hed).text
    return response
