#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import request, render_template, send_file
from ._app import (app, getLogger, conversion, campaign,
                   config, uid_entry, db)
from .models import LogTable
import datetime
import base64
import io
import urllib.parse
import time
import sys


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entry.js')
def entry_js():
    cid = request.args.get('cid')
    filename = 'user_js/' + str(cid) + '.js'

    # cookieからuid読み出し
    uid = request.cookies.get('uid', None)

    # uidがなければ作成
    if not uid:
        uid = '{0:.0f}'.format(time.time()*100)

    # uidを登録
    uid_entry(cid, uid)

    with open(filename, 'r') as f:
        js = f.read()

        # uidを置き換え
        js = js.replace('[!uid]', uid)

        # 画像にタグ埋め込み
        js += 'image.src = location.protocol + "//127.0.0.1:5000/entry?"' \
            + ' + "cid=" + "1" + "&time=" + now.getTime()' \
            + ' + "&url=" + String(window.location).replace("&", "*")' \
            + ' + "&ref=" + String(document.referrer).replace("&", "*")' \
            + ' + "&uid=" + uid'

        if('p' in request.args):
            js += '+ "&param=' + str(request.args.get('p')) + '"'

        js += ";"

    return js


@app.route('/entry')
def entry():
    # 1x1GIF
    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw =='
    gif_str = base64.b64decode(gif)

    url = urllib.parse.urlparse(request.args.get('url'))

    # 拒否
    if url.path in config['ignorepage']:
        return send_file(io.BytesIO(gif_str), mimetype='image/gif')

    url_qs = urllib.parse.parse_qs(url.query.replace('*', '&'))

    # コンバージョン
    if '--debug' in sys.argv:
        if 'param' in request.args:
            conversion(request)
            # 媒体
            if 'ad' in url_qs:
                campaign(url_qs['ad'][0], request)

    query = ''
    for a in request.args:
        query += request.args.get(a) + ', '

    now = datetime.datetime.now()
    ip = request.remote_addr

    # ログ出力
    logger = getLogger(__name__, 'entry.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) + ip + ' - ' + query)

    # DB保存
    row = LogTable(
        cid=request.args.get('cid'),
        uid=request.args.get('uid'),
        ip=ip,
        url=request.args.get('url'),
        referrer=request.args.get('ref'),
        param=request.args.get('param') if 'param' in request.args else None
    )
    LogTable.save_to_db(row)

    return send_file(io.BytesIO(gif_str), mimetype='image/gif')
