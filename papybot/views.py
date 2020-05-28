from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

from .utils.query import Query
from .utils.api import Gooapi, Wikiapi
from .config import map_style, MAPBOX, GOOGLE

from . import app
"""
    Main file of appplication
    the routes
"""

post = {
    'title': 'papy-bot'
}


@app.context_processor
def inject_now():
    """
    Context processor to get the dat/time into the navbar
    Returns:
        datetime
    """
    return {'now': datetime.now()}


@app.context_processor
def map_provider():
    if map_style['OSM']:
        map = 'OSM'
        key = MAPBOX['key']
    else:
        map = 'GOOGLE'
        key = os.environ['GOOGLE_KEY']
    return {'map': map, 'key': key}


@app.route('/')
@app.route('/index/')
def home():
    """
        the homepage
    """
    return render_template("pages/home.html")


@app.route('/about/')
def about():
    post['title'] = "About"
    return render_template("pages/about.html", post=post)


@app.route('/go/')
def go():
    """
        The main page
        question/answer page
    """
    post['title'] = "discuter"
    # if not request.script_root:
    #    request.script_root = url_for('go', _external=True)
    return render_template("pages/go.html", post=post)


@app.errorhandler(404)
def page_not_found(error):
    """
        the 404 page
    """
    post['title'] = "NotFound"
    # the 404 parameter permit to return a real 404 code
    return render_template('errors/404.html', post=post), 404


@app.route("/ajax/", methods=['POST'])
def ajax():
    """
        Ajax function
        Param : The post --> The child question "as is" (format json)
        return (a dict of 2 dicts - google result end wiki result)
        1st The question is 'dejsonified'
        2nd The question is parsed
        3rd The result is send to Google Api
        4th if Google OK the result (name) is passed to the wiki api
    """
    google_error = False
    if request.method == 'POST':
        request_data = json.loads(request.data)
        query = Query(request_data['question'])
        resp = query.parse_query()
        # Google API
        my_gooapi = Gooapi(resp)
        goo_result = my_gooapi.get_json()
        # variable map is used in templates
        map = map_provider()
        # test the google API result
        try:
            goo_result['name']
        except KeyError:
            google_error = True
            goo_result['adress'] = 'Error'
            wiki_result = ""
        # google OK --> WIKI API
        if not google_error:
            my_wikiapi = Wikiapi(goo_result['name'])
            wiki_result = my_wikiapi.get_json()
        # build the result
        resp_dict = jsonify({'goo_result': goo_result, 'wiki_result': wiki_result})
    return resp_dict


@app.route("/goosm/", methods=['POST'])
def goosm():
    """
    Modifiy the map_style from the menu
    """
    if request.method == 'POST':
        if request.data.decode() == 'OSM':
            map_style['OSM'] = True
            map_style['GOOGLE'] = False
        else:
            map_style['OSM'] = False
            map_style['GOOGLE'] = True
    return 'OK'
