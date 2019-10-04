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

with open('config.json', 'r') as f:
    config = json.load(f)


def getLogger(name=__name__, filename=None):
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
    now = datetime.datetime.now()
    ip = request.remote_addr
    conv = request.args.get('param')
    url = urllib.parse.unquote(request.url)

    logger = getLogger('conv', 'conv.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) +
                ip + ' - ' + conv + ' - ' + url)


def campaign(adid, request):
    now = datetime.datetime.now()
    url = request.args.get('url')
    ref = request.args.get('ref')

    # 媒体が定義されていれば処理
    for v in config['campaign'].values():
        if v['ad'] in adid:
            logger = getLogger('campaign', 'campaign.log')
            logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) +
                        str(adid) + ' - ' + url + ' - ' + ref)
