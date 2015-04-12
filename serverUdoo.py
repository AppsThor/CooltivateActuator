__author__ = 'Samuele'

from flask import Flask, jsonify
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttymxc3', 115200, timeout=1)
ser.flushOutput()

current_fan_status = 0
current_irrigation_status = 0
current_light_value = 0

@app.route("/fan", methods=['GET'])
def get_fan_status():
    return jsonify({'status': current_fan_status})


@app.route("/fan/<int:new_fan_status>", methods=['GET'])
def set_fan_status(new_fan_status):
    global current_fan_status
    if new_fan_status > 0:
        current_fan_status = 1
        ser.write("F1")
    else:
        current_fan_status = 0
        ser.write("F0")

    return jsonify({'status': current_fan_status}), 201


@app.route("/irrigation", methods=['GET'])
def get_irrigation_status():
    return jsonify({'status': current_irrigation_status})


@app.route("/irrigation/<int:new_irrigation_status>", methods=['GET'])
def set_irrigation_status(new_irrigation_status):
    if new_irrigation_status > 0:
        global current_irrigation_status
        current_irrigation_status = 1
        ser.write("I1")
    else:
        current_irrigation_status = 0
        ser.write("I0")

    return jsonify({'status': current_irrigation_status}), 201


@app.route("/light", methods=['GET'])
def get_light_status():
    return jsonify({'status': current_light_value})


@app.route("/light/<int:new_light_value>", methods=['GET'])
def set_light_value(new_light_value):
    global current_light_value
    current_light_value = new_light_value

    ser.write("L" + 'current_light_value')

    return jsonify({'status': current_light_value}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0')