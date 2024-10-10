import waitress
from flask import Flask

from . import config, load_configuration, DEFAULT_CONFIGURATION_FILEPATH
from . import controller

load_configuration(DEFAULT_CONFIGURATION_FILEPATH)

app = Flask(__name__)
controller.setup(app)

host = config("flask.host")
port = config("flask.port")

print("Starting server on %s:%s" % (host, port))
waitress.serve(app, host=host, port=port)
