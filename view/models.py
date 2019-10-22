#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ._app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class LogTable(db.Model):
    __tablename__ = 'LogTable'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    cid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    ip = db.Column(db.Text)
    url = db.Column(db.Text)
    referrer = db.Column(db.Text)
    param = db.Column(db.Text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
