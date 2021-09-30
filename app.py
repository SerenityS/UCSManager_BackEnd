import json

from flask import Flask, request
from ucsSql import UcsSql

app = Flask(__name__)


@app.route('/getucs')
def getUcs():
    param = request.args.to_dict()
    if len(param) == 0:
        return 'Error! No parameter found.'

    song_title = param['songTitle']
    song_lv = param['songLv']
    step_maker = param['stepMaker']

    result = UcsSql().findFromSql(song_title, song_lv, step_maker)
    result.sort()

    response = app.response_class(
        response=json.dumps(result, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')

