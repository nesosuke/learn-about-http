import json as j

from flask import Blueprint, jsonify, request
from flask_cors import CORS

bp = Blueprint('bp', __name__)
CORS(bp)


@bp.route('/', methods=['GET', 'POST'])
def index():
    const_data = {
        'messege': 'Hello World!'
    }
    return_data = {
        'const_data': const_data,
    }
    if request.method == 'GET':
        '''
        GETにはリクエストボディにデータがない
        '''
        return jsonify(return_data)

    if request.get_json() is None:
        json = 'json is None'
    json = request.get_json()

    if request.get_data() is None:
        data = 'data is None'
    data = request.get_data().decode('utf-8')

    return_data['json'] = json
    return_data['data'] = data

    # return_data=j.dumps(return_data)
    return_data = jsonify(return_data)

    return return_data
