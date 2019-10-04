#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import logging
import json
import datetime
import urllib

app = Flask(__name__, template_folder='../templates',
            static_folder="../static")

loggers = {}

# 設定ファイル読み込み
with open('config.json', 'r') as f:
    config = json.load(f)


def getLogger(name=__name__, filename=None):
    # 任意のLoggerを取得

    global loggers

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if(filename):
        handler = logging.FileHandler(filename, 'a')
    else:
        handler = logging.StreamHandler()

    logger.addHandler(handler)
    loggers[name] = logger
    return logger


def conversion(request):
    # コンバージョンをログに保存

    now = datetime.datetime.now()
    ip = request.remote_addr
    conv = request.args.get('param')
    url = urllib.parse.unquote(request.url)

    logger = getLogger('conv', 'conv.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) +
                ip + ' - ' + conv + ' - ' + url)


def campaign(adid, request):
    # 広告流入をログに保存

    now = datetime.datetime.now()
    url = request.args.get('url')
    ref = request.args.get('ref')
    conv = request.args.get('param')

    # 媒体が定義されていれば処理
    for v in config['campaign']:
        if v['ad'] == adid and v['cv'] == conv:
            logger = getLogger('campaign', 'campaign.log')
            logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) +
                        str(v['id']) + ' - ' + v['ad'] + ' - ' +
                        url + ' ' + ref)


def uid_entry(cid, uid):
    # uidを保存しているファイル読み出し
    try:
        with open('member.json', 'r') as f:
            j = json.load(f)
    except FileNotFoundError:
        j = {}

    # cidが登録されていなければ作成
    if cid not in j:
        j[cid] = []

    # uidがデータ内に含まれていなければ追加
    if uid not in j[cid]:
        with open('member.json', 'w') as f:
            j[cid].append(uid)
            json.dump(j, f, indent=2)
