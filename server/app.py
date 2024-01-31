#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hero.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Heroes(Resource):
    def get (self):
        hero_data = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in Hero.query.all()]
        return make_response(jsonify(hero_data), 200)


api.add_resource(Heroes, '/heroes')


class HeroById(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()

        if not hero:
            return make_response(jsonify({"message": "Hero not found"}), 404)

        
        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": []
        }

        
        for power in hero.powers:
            power_data = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            hero_data["powers"].append(power_data)

        return make_response(jsonify(hero_data), 200)


api.add_resource(HeroById, '/heroes/<int:id>')


class Powers(Resource):
    def get(self):
        power_data = [
            {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            for power in Power.query.all()
        ]
        return make_response(jsonify(power_data), 200)


api.add_resource(Powers, '/powers')


class PowerById(Resource):
    def get(self,id):
        power= Power.query.filter_by(id=id).first()
        if not power:
            return make_response(jsonify({"message": "Power not found"}))
        power_data={
            "id":power.id,
            "name":power.name,
            "description":power.description
        }
        return make_response(jsonify(power_data), 200)
    def patch(self, id):
        power = Power.query.filter_by(id=id).first()
        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)

        # Update the power description if provided in the request
        if 'description' in request.json:
            power.description = request.json['description']

            
            db.session.commit()
            return make_response(jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
            }), 200)
           
        else:
            return make_response(jsonify({"errors": ["Description not provided"]}), 400)
        
        
api.add_resource(PowerById, '/powers/<int:id>')


class HeroPowerResource(Resource):
    def post(self):
        data = request.json
        strength = data.get('strength')
        power_id = data.get('power_id')
        hero_id = data.get('hero_id')

        if not (strength and power_id and hero_id):
            return make_response(jsonify({"errors": ["Missing required fields"]}), 400)

        power = Power.query.get(power_id)
        hero = Hero.query.get(hero_id)

        if not (power and hero):
                return make_response(jsonify({"errors": ["Invalid Power or Hero ID"]}), 400)

        hero_power = HeroPower(strength=strength, hero=hero, power=power)

        
        db.session.add(hero_power)
        db.session.commit()
        

        return make_response(jsonify({"message": "HeroPower created successfully"}), 201)
api.add_resource(HeroPowerResource, '/hero_powers')

if __name__ == '__main__':
    app.run(port=5555,debug=True)
