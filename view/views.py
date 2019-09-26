from flask import request, render_template, send_file
from view._app import app, getLogger
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

        js += 'image.src = location.protocol + "//127.0.0.1:5000/entry?"' \
            + ' + "cid=" + "1" + "&time=" + now.getTime()' \
            + ' + "&url=" + window.location + "&ref=" + document.referrer'

        if('p' in request.args):
            js += '+ "&param=' + str(request.args.get('p')) + '"'

        js += ";"

    return js


@app.route('/entry')
def entry():
    ip = request.remote_addr
    query = ''
    for a in request.args:
        query += request.args.get(a) + '*'

    if 'param' in request.args:
        print(request.args.get('param'))

    # 時刻取得
    now = datetime.datetime.now()

    # ログ出力
    logger = getLogger(__name__, 'entry.log')
    logger.info('{0:%Y/%m/%d %H:%M:%S} - '.format(now) + ip + ' - ' + query)

    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw =='
    gif_str = base64.b64decode(gif)
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')
