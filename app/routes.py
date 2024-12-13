from flask import Blueprint, jsonify, request

bp = Blueprint('routes', __name__)

# Lista de autos como base de datos simulada
autos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020, "precio": 20000, "color": "Blanco"},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 22000, "color": "Negro"},
    {"id": 3, "marca": "Ford", "modelo": "Mustang", "año": 2021, "precio": 35000, "color": "Rojo"},
    {"id": 4, "marca": "Chevrolet", "modelo": "Camaro", "año": 2022, "precio": 40000, "color": "Azul"},
    {"id": 5, "marca": "BMW", "modelo": "Serie 3", "año": 2021, "precio": 45000, "color": "Gris"},
    {"id": 6, "marca": "Audi", "modelo": "A4", "año": 2020, "precio": 42000, "color": "Blanco"},
    {"id": 7, "marca": "Mercedes-Benz", "modelo": "C-Class", "año": 2021, "precio": 48000, "color": "Negro"},
    {"id": 8, "marca": "Nissan", "modelo": "Altima", "año": 2018, "precio": 18000, "color": "Plateado"},
    {"id": 9, "marca": "Hyundai", "modelo": "Elantra", "año": 2019, "precio": 17000, "color": "Azul"},
    {"id": 10, "marca": "Kia", "modelo": "Optima", "año": 2020, "precio": 19000, "color": "Rojo"},
    {"id": 11, "marca": "Mazda", "modelo": "Mazda3", "año": 2021, "precio": 21000, "color": "Negro"},
    {"id": 12, "marca": "Subaru", "modelo": "Impreza", "año": 2021, "precio": 23000, "color": "Blanco"},
    {"id": 13, "marca": "Tesla", "modelo": "Model 3", "año": 2022, "precio": 50000, "color": "Negro"},
    {"id": 14, "marca": "Volkswagen", "modelo": "Jetta", "año": 2019, "precio": 20000, "color": "Gris"},
    {"id": 15, "marca": "Volvo", "modelo": "S60", "año": 2020, "precio": 30000, "color": "Blanco"},
    {"id": 16, "marca": "Lexus", "modelo": "IS", "año": 2021, "precio": 40000, "color": "Azul"},
    {"id": 17, "marca": "Jaguar", "modelo": "XE", "año": 2020, "precio": 42000, "color": "Negro"},
    {"id": 18, "marca": "Porsche", "modelo": "911", "año": 2022, "precio": 90000, "color": "Rojo"},
    {"id": 19, "marca": "Ferrari", "modelo": "Portofino", "año": 2022, "precio": 200000, "color": "Rojo"},
    {"id": 20, "marca": "Lamborghini", "modelo": "Huracán", "año": 2022, "precio": 300000, "color": "Amarillo"}
]

# Rutas de nuestro servicio
@bp.route('/autos', methods=['GET'])
def get_autos():
    return jsonify(autos)

@bp.route('/autos/<int:auto_id>', methods=['GET'])
def get_auto(auto_id):
    auto = next((auto for auto in autos if auto['id'] == auto_id), None)
    if auto:
        return jsonify(auto)
    return jsonify({ "error": "Auto no encontrado" }), 404

@bp.route('/autos', methods=['POST'])
def add_auto():
    nuevo_auto = request.get_json()
    nuevo_auto['id'] = len(autos) + 1
    autos.append(nuevo_auto)
    return jsonify(autos), 201

@bp.route('/autos/<int:auto_id>', methods=['DELETE'])
def del_auto(auto_id):
    global autos
    autos = [auto for auto in autos if auto['id'] != auto_id]
    return jsonify({ "message": "Auto eliminado" })