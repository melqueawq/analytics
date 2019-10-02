#!/usr/bin/env python
# -*- coding:utf-8-*-

from flask import Flask
import logging
import json
import os
import datetime

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


def conversion(conv):
    # jsonかdbでとる
    now = datetime.datetime.now()

    logger = getLogger('conv', 'conv.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) + conv)


def campaign(adid, ref):
    now = datetime.datetime.now()
    print(adid)
    logger = getLogger('campaign', 'campaign.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) +
                str(adid) + ' - ' + str(ref))
