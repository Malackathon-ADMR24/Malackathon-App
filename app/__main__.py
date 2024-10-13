import sys

import waitress
from flask import Flask

from . import config, load_configuration, DEFAULT_CONFIGURATION_FILEPATH
from . import controller, db, job

if len(sys.argv) > 1:
    configfile = sys.argv[1]
else:
    configfile = DEFAULT_CONFIGURATION_FILEPATH

load_configuration(configfile)

db.databaseconnection.detect_driver()
db.migration.migrate()

app = Flask(__name__)
controller.setup(app)

host = config("flask.host")
port = config("flask.port")
debug = str(config("flask.debug")).lower() == "true"

print("Starting jobs")
job.start_jobs()

print("Starting server on %s:%s" % (host, port))
if debug:
    app.run(host=host, port=port, debug=True)
else:
    waitress.serve(app, host=host, port=port)
