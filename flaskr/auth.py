import requests


def auth(token, memberID):
    hed = {'Authorization': 'Bearer ' + token}
    data = {'member': memberID}
    url = 'https://perun.elixir-czech.cz/oauth/rpc/json/authzResolver/isFacilityAdmin'
    response = requests.post(url, json=data, headers=hed)
    return response.text
