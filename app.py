from flask import Flask, jsonify, render_template, request
import json
import requests

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
"""
def get_client_location(ip):
    resp = requests.get(f'https://ipinfo.io/{ip}/json')
    dt = resp.json()
    if dt['bogon']:
        addr="Your Mom"
    else:
        addr=f"{dt['city']},{dt['region']},{dt['country']} or {dt['loc']}"
    return addr
"""
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
    content={'title':'Welcome to Just Arnav', 'links':links}# 'client_loc':get_client_location(request.environ['REMOTE_ADDR'])}
    return render_template('index.html', content=content)

@app.route('/json')
def index_json():
    with open('links.json','r') as f: links=json.load(f)
    resp = {
                'status':['Working',True, 200],
                'message':{
                        'text':"""
Hi, I am Arnav Ghosh and This is my Website and you are welcome.
Caution use JQ if you are in a Terminal
                        """,
                        'links':links
                    }
            }
    return jsonify(resp)

@app.route('/terminal')
def index_terminal():
    with open('term.txt', 'rt') as f: termtext = f.read()
    return termtext

if __name__=='__main__':
    app.run()
