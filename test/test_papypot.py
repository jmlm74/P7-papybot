import requests
import json

import papybot.utils.query as query
import papybot.utils.api as api
from  papybot import app

# test homepage return 200
def test_index_page_return200():
    rc = requests.get("http://127.0.0.1:5000/index/")
    assert rc.status_code == 200

# test 404 page return 404 and not 200
def test_foobar_return404():
    rc = requests.get("http://127.0.0.1:5000/foobar/")
    assert rc.status_code == 404


# test parser stand alone
def test_parser_ok():
    req = query.Query("Salut GrandPy ! sais tu quelle est la capitale de la Bulgarie ? Merci !")
    result = req.parse_query()
    assert result == "capitale bulgarie"

# test gooapi
def test_gooapi_ok(monkeypatch):

    class MockResp:
        """
        Mock the requests.get
        status_code is the http code response
        json() is to mock  requests.json() and simulate the json response of requests.get
            The return is the same as requests.get --> get in a sample file in static/api
        """
        def __init__(self):
            self.status_code = 200

        def json(*args):
            fic_json = str(app.root_path) + '/static/api/1.json'
            json_data = open(fic_json, 'r')
            text = json_data.read()
            json_data.close()
            json_response = {}
            json_response = json.loads(text)
            return json_response

    # the file 1.json contains the real return of google geocode for the address of the eiffel tower
    testgooapi = api.Gooapi('adresse tour eiffel')

    def mock_request_get(url):
        mock_resp = MockResp()
        return mock_resp

    monkeypatch.setattr('requests.get', mock_request_get)
    tab_result = testgooapi.get_json()
    assert tab_result[0]['latitude'] == 46.8077191
