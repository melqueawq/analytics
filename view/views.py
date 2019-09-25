from flask import request, render_template, url_for, send_file
from view import app
from logging import getLogger, FileHandler, DEBUG
import datetime
import base64
import io


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entry.js')
def entry_js():
    cid = request.args.get('cid')
    filename = 'user_js/' + str(cid) + '.js'
    with open(filename, 'r') as f:
        js = f.read()
    return js


@app.route('/entry')
def entry():
    ip = request.remote_addr
    query = request.query_string.decode('UTF-8')

    # 時刻取得
    now = datetime.datetime.now()

    # ログ出力
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    fh = FileHandler('entry.log', 'a')
    logger.addHandler(fh)
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) + ip + ' - ' + query)

    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw =='
    gif_str = base64.b64decode(gif)
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')
