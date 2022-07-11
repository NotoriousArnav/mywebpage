from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')

def get_client_location(ip):
    resp = requests.get(f'https://ipinfo.io/{ip}/json')
    dt = resp.json()
    if dt['bogon']:
        addr="Your Mom"
    else:
        addr=f"{dt['city']},{dt['region']},{dt['country']} or {dt['loc']}"
    return addr

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
    content={'title':'Welcome to Just Arnav', 'links':links, 'client_loc':get_client_location(request.environ['REMOTE_ADDR'])}
    return render_template('index.html', content=content)