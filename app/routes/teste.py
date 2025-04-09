from flask import Blueprint, request, jsonify

route_test = Blueprint('test', __name__)

@route_test.route('/hello-world', methods=['GET'])
def teste():
    return "<h1>Hello World</h1>", 200
