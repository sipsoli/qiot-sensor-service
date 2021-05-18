#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

import pollution
import system
import os
import uuid
import gas
import atexit
import lcd

atexit.register(lcd.stop)

app = Flask(__name__)
app.register_blueprint(get_swaggerui_blueprint('/swagger', '/static/swagger.json', config={'app_name': "qiot-sensor-service"}), url_prefix='/swagger')


@app.route('/api/system/id', methods=['GET'])
def get_system_id():
    return jsonify(system.get_serial_number())


@app.route('/api/sensors/gas', methods=['GET'])
def collect_gas_data():
    return jsonify(gas.get_gas_data())


@app.route('/api/sensors/pollution', methods=['GET'])
def collect_pollution_data():
    return jsonify(pollution.get_all_particulates())


@app.after_request
def apply_response_headers(response):
    response.headers["X-Correlation-Id"] = uuid.uuid4()
    return response


@app.errorhandler(404)
def resource_not_found(e):
    error = "{0}".format(e)
    return jsonify({"error": error}), 404


if __name__ == '__main__':
    lcd.draw_message()
    app.run(
        host=os.getenv('FLASK_APP_HOST'),
        port=os.getenv('FLASK_APP_PORT'),
        debug=os.getenv('FLASK_APP_DEBUG')
    )
