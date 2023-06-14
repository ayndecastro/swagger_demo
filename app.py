import argparse
import os
from flask import Flask, jsonify, make_response
from flask_swagger_ui import get_swaggerui_blueprint

APP = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger-UI Demo"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

# Define a simple route that returns a JSON response


@APP.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    APP.run()
