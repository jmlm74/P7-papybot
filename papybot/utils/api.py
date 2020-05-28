import random
import requests
import os

from papybot.config import GOOGLE, WIKI, MESSAGES


class Api:
    """
    mother class of the apis 
    Init the query and make the HTTP request
    """

    def __init__(self, query):
        self.query = query
        self.query = self.query.replace(" ", "+")
        self.url_complete = ""

    def api_get_json(self):
        """
            Params : none
            Return : the response <object> of the request (json format for datas)
        """
        return requests.get(self.url_complete)


class Gooapi(Api):
    """
    Google API
    """
    def __init__(self, query):
        """
            Params : The parsed query
            Return : none
            Use the Api (mother class) init
            Build the complete url for the request
        """
        Api.__init__(self, query)
        self.url_complete = GOOGLE["url"] + self.query + "&key=" + os.environ["GOOGLE_KEY"]

    def get_json(self):
        """
            Params : None
            Return : dict of the result of the request
            Call the api_get_json function of the mother class
            Test the reponse Return Code and parse the datas
            use the 'findplacefromtext' function in google API
        """
        result = {}
        # get the result
        response = self.api_get_json()
        # build the result
        if response.status_code == 200:
            text = response.json()
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
    """
        Wiki API
    """
    def __init__(self, query):
        """
            Params : the query --> result of google API (name)
            Return : none
            Use the Api (mother class) init
            Build the complete url for the request
        """
        Api.__init__(self, query)
        self.url_complete = WIKI['url1'] + query

    def get_json(self):
        """
            Params : None
            Return : dict of the result of the request
            The request is done in 2 times : 
            - 1st get the page_id using the 'list=search' function 
            - 2nd rebuild the URL and then get the page id from 1st then get the detail via 'prop=extracts'
            Call the api_get_json twice function of the mother class
            Test the reponse Return Code and parse the datas 
        """
        result = {}
        page_id = ""
        # 1st - get page id
        response = self.api_get_json()
        if response.status_code != 200:
            result['error'] = True
            return result
        text = response.json()
        t = text['query']['search'][0]
        title = t['title']
        page_id = str(t['pageid'])
        # 2nd Buil url and get the extract of the page_id
        self.url_complete = WIKI['url3'] + page_id
        response = self.api_get_json()
        # build the result
        if response.status_code != 200:
            result['error'] = True
            return result
        text = response.json()
        extract = text['query']['pages'][page_id]['extract']
        result['error'] = False
        result['title'] = title
        result['extract'] = extract
        result['id'] = page_id
        result['msg'] = random.choice(MESSAGES)
        return result
