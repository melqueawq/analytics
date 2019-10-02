#!/usr/bin/env python
# -*- coding:utf-8-*-

from flask import request, render_template, send_file
from view._app import app, getLogger, conversion, campaign, config
import datetime
import base64
import io
import json
import urllib.parse


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entry.js')
def entry_js():
    cid = request.args.get('cid')
    filename = 'user_js/' + str(cid) + '.js'

    with open(filename, 'r') as f:
        js = f.read()

        js += 'image.src = location.protocol + "//127.0.0.1:5000/entry?"' \
            + ' + "cid=" + "1" + "&time=" + now.getTime()' \
            + ' + "&url=" + window.location + "&ref=" + document.referrer'

        if('p' in request.args):
            js += '+ "&param=' + str(request.args.get('p')) + '"'

        js += ";"

    return js


@app.route('/entry')
def entry():
    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw =='
    gif_str = base64.b64decode(gif)

    url = urllib.parse.urlparse(request.args.get('url'))
    if url.path in config['ignorepage']:
        return send_file(io.BytesIO(gif_str), mimetype='image/gif')

    urlqs = urllib.parse.parse_qs(url.query)
    if 'ad' in urlqs:
        campaign(urlqs['ad'], request.args.get('ref'))

    ip = request.remote_addr
    query = ''
    for a in request.args:
        query += request.args.get(a) + '*'

    if 'param' in request.args:
        conversion(request.args.get('param'))

    # 時刻取得
    now = datetime.datetime.now()

    # ログ出力
    logger = getLogger(__name__, 'entry.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) + ip + ' - ' + query)
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')
