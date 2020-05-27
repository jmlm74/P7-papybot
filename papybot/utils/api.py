from papybot.config import GOOGLE, WIKI
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

    def get_json(self):
        result = {}
        print(self.url_complete)
        # ! response = requests.get(self.url_complete)
        response = self.api_get_json()
        # *fic_json = str(app.root_path) + '/static/api/1.json'
        if response.status_code == 200:
        # *if True:
            text = response.json()
            # *with open(fic_json) as json_data:
            # *    text = json.load(json_data)
            if text['status'] != 'OK':
                result['address'] = 'Error'
            else:
                t = text['candidates'][0]
                result['address'] = t['formatted_address']
                result['latitude'] = t['geometry']['location']['lat']
                result['longitude'] = t['geometry']['location']['lng']
                result['name'] = t['name']
        else:
            result['address'] = 'Error'
        return result


class Wikiapi(Api):

    def __init__(self, query):
        Api.__init__(self, query)
        self.url_complete = WIKI['url1'] + query

    def get_json(self):
        result = {}
        page_id = ""
        response = self.api_get_json()
        if response.status_code != 200:
            result['error'] = True
            return result
        text = response.json()
        t = text['query']['search'][0]
        title = t['title']
        page_id = str(t['pageid'])
        self.url_complete = WIKI['url3'] + page_id
        response = self.api_get_json()
        if response.status_code != 200:
            result['error'] = True
            return result
        text = response.json()
        extract = text['query']['pages'][page_id]['extract']
        result['error'] = False
        result['title'] = title
        result['extract'] = extract
        result['id'] = page_id
        return result
