from flask import request, jsonify
import config

from config import db, ma

connex_app = config.connex_app





# Animal Class/Model
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(200))
    animal_type = db.Column(db.String(20))
    location = db.Column(db.String(200))
    hasOwner = db.Column(db.String(200), default="No Owner")
    status = db.Column(db.Boolean, default=False)

    def __init__(self, name, description, animal_type, location, hasOwner, status):
        self.name = name
        self.description = description
        self.animal_type = animal_type
        self.location = location
        self.hasOwner = hasOwner
        self._status = status


# Animal Schema
class AnimalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'animal_type', 'location', 'hasOwner', 'status')


# Init schema
animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)


# Create a Pet
@connex_app.route('/pets/', methods=['POST'])
def add_animal():
    name = request.json['name']
    description = request.json['description']
    animal_type = request.json['animal_type']
    location = request.json['location']
    hasOwner = request.json['hasOwner']
    new_status = request.json['status']

    new_animal = Animal(name, description, animal_type, location, hasOwner, new_status)

    db.session.add(new_animal)
    db.session.commit()

    return animal_schema.jsonify(new_animal)


# Get All Animals
@connex_app.route('/pets/', methods=['GET'])
def get_animal():
    all_animal = Animal.query.all()
    result = animals_schema.dump(all_animal)
    return jsonify(result)


# Get Single Animal
@connex_app.route('/pets/<id>/', methods=['GET'])
def post_animal(id):
    animal = Animal.query.get(id)
    return animal_schema.jsonify(animal)


# Update a l
@connex_app.route('/pets/<id>/', methods=['PUT'])
def update_animal(id):
    animal = Animal.query.get(id)

    name = request.json['name']
    description = request.json['description']
    animal_type = request.json['animal_type']
    location = request.json['location']
    hasOwner = request.json['hasOwner']
    set_status = request.json['status']

    animal.name = name
    animal.description = description
    animal.animal_type = animal_type
    animal.location = location
    animal._status = set_status
    animal.hasOwner = hasOwner

    db.session.commit()

    return animal_schema.jsonify(animal)


# Delete Animal
@connex_app.route('/pets/<id>/', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get(id)
    db.session.delete(animal)
    db.session.commit()

    return animal_schema.jsonify(animal)
