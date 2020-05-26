from papybot.config import GOOGLE
import requests
import json
from papybot import app


class Api:

    def __init__(self, query):
        self.query = query
        self.query = self.query.replace(" ", "+")
        self.url_complete = ""

    def api_get_json(self):
        resp = requests.get(self.url_complete)
        return resp


class Gooapi(Api):

    def __init__(self, query):
        Api.__init__(self, query)
        self.url_complete = GOOGLE["url"] + self.query + "&key=" + GOOGLE["key"]
        # self.url_complete = GOOGLE["url"] + self.query + "&key=" +"key"
        # @property

    def get_json(self):
        tab_result = []
        result = {}
        # # response = requests.get(self.url_complete)
        fic_json = str(app.root_path) + '/static/api/2.json'
        # #if response.status_code == 200:
        if True:
            # #text = response.json()
            with open(fic_json) as json_data:
                text = json.load(json_data)
            print("Apres response.json() : %s" % text)
            if text['status'] != 'OK':
                result['address'] = None
                tab_result.append(result)
            for t in text['results']:
                print("formatted address : %s " % t['formatted_address'])
                print("latitude :  %f" % t['geometry']['location']['lat'])
                print("longitude :  %f" % t['geometry']['location']['lng'])
                result['address'] = t['formatted_address']
                result['latitude'] = t['geometry']['location']['lat']
                result['longitude'] = t['geometry']['location']['lng']
                tab_result.append(result)
                result = {}
        else:
            result['address'] = 'Error'
            tab_result.append(result)
        print(tab_result)
        return tab_result
