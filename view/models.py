#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ._app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class LogTable(db.Model):
    __tablename__ = 'LOG'
    date = db.Column(db.Datetime, default=datetime.now())
    cid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    ip = db.Column(db.Text)
    url = db.Column(db.Text)
    referrer = db.Column(db.Text)
    conv = db.Column(db.Text)
    ad = db.Column(db.Text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
