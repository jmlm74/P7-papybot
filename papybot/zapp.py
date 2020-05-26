from flask import Flask, render_template, abort, request, url_for, jsonify
from datetime import datetime
import json
"""
    Main file of appplication
    the routes
"""

app = Flask(__name__)

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
    return render_template("pages/about.html",post=post)


@app.route('/contact/')
def contact():
    return render_template("pages/contact.html")


@app.route('/go/')
def go():
    """
        The main page
        question/answer page
    """
    post['title'] = "discuter"
    if not request.script_root:
        request.script_root = url_for('go', _external=True)
    return render_template("pages/go.html", post=post)


@app.errorhandler(404)
def page_not_found(error):
    post['title'] = "NotFound"
    return render_template('errors/404.html', post=post), 404  # les 2nd 404 permet de renvoyer un VRAI 404 !


@app.route("/ajax", methods=['POST'])
def ajax():
    if request.method == 'POST':
        print('POST')
        req_data = json.loads(request.data)
        

    return jsonify({'rep': "pas de reponse"})


if __name__ == "__main__":
    app.run(debug=True)
