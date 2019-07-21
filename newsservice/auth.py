import requests


def auth(facility, token):

    hed = {'Authorization': 'Bearer ' + token}
    data = {'facility': facility}
    url = 'https://perun.elixir-czech.cz/oauth/rpc/json/authzResolver/isFacilityAdmin'
    response = requests.post(url, json=data, headers=hed).text
    return response
