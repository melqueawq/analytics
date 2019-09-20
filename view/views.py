from flask import request, render_template, url_for, send_from_directory
from view import app
import datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entry.js')
def entry_js():
    cid = request.args.get('cid')
    filename = 'user_js/' + str(cid) + '.js'
    with open(filename, 'r') as f:
        js = f.read()
    return js


@app.route('/entry')
def entry():
    ip = request.remote_addr
    print('ip', ip)
    now = datetime.datetime.now()
    query = request.query_string.decode('UTF-8')

    # with open('../entry.log', 'a') as f:
    #    print('{0:%Y/%m/%d %h:%M:%s - }'.format(now), ip, '-', query, file=f)

    return send_from_directory('../static/image/', filename='1x1.gif')
