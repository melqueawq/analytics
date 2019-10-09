#!/usr/bin/env python
# -*- coding:utf-8 -*-

from view._app import app
import view.views


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
