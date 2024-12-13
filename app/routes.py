from flask import Blueprint, jsonify, request
import json
from datetime import datetime

bp = Blueprint('routes', __name__)

def load_data():
    with open('db.json', encoding='utf-8') as file:
        return json.load(file)
    
def save_data(db):
    with open('db.json', 'w', encoding='utf-8') as file:
        json.dump(db, file, indent=4)
    
db = load_data()

# Rutas de nuestro servicio
@bp.route('/products', methods=['GET'])
def get_autos():
    return jsonify(db['products'])


@bp.route('/products/<string:category>', methods=['GET'])
def get_autos_by_category(category):
    products = [product for product in db['products'] if product['category'] == category.lower()]
    return jsonify(products)


@bp.route('/orders', methods=['POST'])
def add_order():
    order = request.get_json()
    order['id'] = len(db['orders']) + 1
    order['date_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db['orders'].append(order)
    save_data(db)
    return jsonify(db['orders']), 201


@bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = next((order for order in db['orders'] if order['id'] == order_id), None)
    if order:
        # Valores que no se deben de actualizar aunque el usuario las proporcione (id, date_created)
        request.get_json().pop('id', None)
        request.get_json().pop('date_created', None)

        order['date_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        order.update(request.get_json())
        save_data(db)
        return jsonify(order)
    return jsonify({ "error": "Orden no encontrada" }), 404


@bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = next((order for order in db['orders'] if order['id'] == order_id), None)
    if order:
        db['orders'].remove(order)
        save_data(db)
        return jsonify({ "message": "Orden eliminada correctamente" })
    return jsonify({ "error": "Orden no encontrada" }), 404


@bp.route('/authenticate', methods=['POST'])
def authenticate():
    credentials = request.get_json()

    user = next((user for user in db['users'] if user['username'] == credentials['username']), None)
    if user and user['password'] == credentials['password']:
        return jsonify({ "message": "Usuario autenticado correctamente" })
    return jsonify({ "error": "Usuario o contraseña incorrectos" }), 401