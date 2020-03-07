# Created by ruben.quadros on 26/02/20.

from flask import Flask, request, jsonify
import json
import threading
from bartender import Bartender

app = Flask(__name__)
bartender = Bartender()


@app.route('/')
def index():
    return "Initializing..."


# run Flask app
if __name__ == "__main__":
    app.run()


@app.route('/make_drink', methods=['POST'])
def make_drink():
    lock = threading.Lock()
    drink_name = request.json['name']
    data = json.load(open('drinks.json'))
    response = "No drinks found"
    status = 404
    with lock:
        for drink in data['drinks']:
            if drink_name == drink['name']:
                pins = bartender.get_pins(drink['ingredients'])
                quantities = bartender.get_quantity(drink['ingredients'])
                bartender.pour_drink(pins, quantities)
                status = 200
                response = "Making your drink"
        return jsonify(
            status=status,
            message=response
        )


@app.route('/custom_drink', methods=['POST'])
def custom_drink():
    print("Making custom drink")
    return "Making custom drink"
