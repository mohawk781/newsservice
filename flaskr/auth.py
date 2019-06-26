import requests


def auth(facility, token, memberid):

    hed = {'Authorization': 'Bearer ' + token}
    data = {'member': memberid}
    url = 'https://perun.elixir-czech.cz/oauth/rpc/json/authzResolver/isFacilityAdmin(' + facility + ')'
    response = requests.post(url, json=data, headers=hed)
    return response.text
