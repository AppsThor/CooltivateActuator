#!/usr/bin/env python

__author__ = 'Samuele'

from flask import Flask, jsonify
import mraa
# import SocketServer

app = Flask(__name__)

current_fan_status = 0
current_irrigation_status = 0
current_light_value = 0

led = mraa.Gpio(4)
led.dir(mraa.DIR_OUT)


@app.route("/fan", methods=['GET'])
def get_fan_status():
    return jsonify({'status': current_fan_status})


@app.route("/fan/<int:new_fan_status>", methods=['POST'])
def set_fan_status(new_fan_status):
    if new_fan_status > 0:
        current_fan_status = 1
    else:
        current_fan_status = 0
    return jsonify({'status': current_fan_status}), 201


@app.route("/irrigation", methods=['GET'])
def get_irrigation_status():
    return jsonify({'status': current_irrigation_status})


@app.route("/irrigation/<int:new_irrigation_status>", methods=['POST'])
def set_irrigation_status(new_irrigation_status):
    if new_irrigation_status > 0:
        current_irrigation_status = 1
    else:
        current_irrigation_status = 0

    return jsonify({'status': current_irrigation_status}), 201


@app.route("/light", methods=['GET'])
def get_light_status():
    return jsonify({'status': current_light_value})


@app.route("/light/<int:new_light_value>", methods=['POST'])
def set_light_value(new_light_value):
    current_light_value = new_light_value
    return jsonify({'status': current_light_value}), 201


@app.route("/led/on", methods=['GET'])
def turn_on_led():
    led.write(1)
    return jsonify({'status', 'LED ON'}), 201


@app.route("/led/off", methods=['GET'])
def turn_off_led():
    led.write(0)
    return jsonify({'status', 'LED OFF'}), 201


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # HOST, PORT = "192.168.3.7", 5000
    # Create the server, binding to localhost on port 5000
    # server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    # server.serve_forever()