from flask import Blueprint, request, jsonify
from app.services.service_user import create_user

route_users = Blueprint('users', __name__)

@route_users.route('/create-user', methods=['POST'])
def create_user_route():
    data = request.get_json()
    
    try:
       result = create_user(data)
       return jsonify(result, 201)
    except Exception as error: 
        return jsonify({"erro": str(error), "mensage": "Erro interno do servidor"}), 500
