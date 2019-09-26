from flask import Flask
import logging

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
