""" Application Entrypoint """
from flask import Flask
from flask_cors import CORS

from controller import API

app = Flask(__name__)  # pylint:disable=invalid-name
CORS(app)
API.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
