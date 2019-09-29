from flask import Flask
import logging
import json
import os

app = Flask(__name__, template_folder='../templates',
            static_folder="../static")

loggers = {}


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
    cvdata = {}
    if os.path.exists("conversion.json"):
        with open("conversion.json", 'r') as f:
            cvdata = json.load(f)

    if conv in cvdata:
        cvdata[conv] += 1
    else:
        cvdata[conv] = 1

    with open("conversion.json", 'w') as f:
        json.dump(cvdata, f)
