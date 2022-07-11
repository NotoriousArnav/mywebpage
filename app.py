from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def index():
    with open('links.json','r') as f: links=json.load(f)
    content={'title':'Welcome to Just Arnav', 'links':links}
    return render_template('index.html', content=content)