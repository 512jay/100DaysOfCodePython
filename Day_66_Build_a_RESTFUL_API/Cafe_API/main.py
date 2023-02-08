import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"{self.name}"

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # random_cafe_dict = {
    #     "cafe": {
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #         "has_sockets": random_cafe.has_sockets,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "id": random_cafe.id,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "map_url": random_cafe.map_url,
    #         "name": random_cafe.name,
    #         "seats": random_cafe.seats,
    #     }
    # }
    # cafe_dictionary = dict(random_cafe.__dict__)
    # del cafe_dictionary["_sa_instance_state"]
    return jsonify(cafe=random_cafe.to_dict())

    # return jsonify(random_cafe_dict)
    # return render_template("random.html", cafe=random_cafe)


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    # cafes_dict = []
    # for cafe in cafes:
    #     cafes_dict.append(cafe.to_dict())
    # return jsonify(cafes=cafes_dict)
    # Here is a good example of a list comprehension replacing a loop.
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
