from flask import Blueprint, jsonify, request, abort
from app.models import Hero, Power, HeroPower
from app import db

main = Blueprint('main', __name__)

# GET /heroes
@main.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

# GET /heroes/<id>
@main.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

# GET /powers
@main.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

# GET /powers/<id>
@main.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

# PATCH /powers/<id>
@main.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        description = data.get('description', None)
        if description and len(description) >= 20:
            power.description = description
            db.session.commit()
            return jsonify(power.to_dict()), 200
        return jsonify({"errors": ["validation errors"]}), 400
    return jsonify({"error": "Power not found"}), 404

# POST /hero_powers
@main.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if strength not in ['Strong', 'Average', 'Weak']:
        return jsonify({"errors": ["Invalid strength"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not hero or not power:
        return jsonify({"errors": ["Invalid hero or power"]}), 400

    new_hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify(new_hero_power.to_dict()), 201
