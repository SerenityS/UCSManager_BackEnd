import json

from flask import Flask, request
from ucsSql import UcsSql

app = Flask(__name__)


@app.route('/getucs')
def getUcs():
    param = request.args.to_dict()
    if len(param) == 0:
        return 'Error! No parameter found.'

    if param['songTitle'] != '':
        song_title = param['songTitle']
    else:
        song_title = 'None'
    if param['songLv'] != '':
        song_lv = param['songLv']
    else:
        song_lv = 'None'
    if param['stepArtist'] != '':
        step_maker = param['stepArtist']
    else:
        step_maker = 'None'

    result = UcsSql().findFromSql(song_title, song_lv, step_maker)

    response = app.response_class(
        response=json.dumps(result, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
