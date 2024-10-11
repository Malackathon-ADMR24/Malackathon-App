import os

import yaml

DEFAULT_CONFIGURATION_FILEPATH = "configuration.dev.yml"

_configuration_object = {}


def load_configuration(filepath: str):
    global _configuration_object
    with open(filepath) as fh:
        _configuration_object = yaml.load(fh, yaml.BaseLoader)


def config(path):
    current_object = _configuration_object
    steps = path.split(".")
    for step in steps:
        print("GET CONFIG ", current_object, step)
        current_object = current_object[step]

    if type(current_object) is str and current_object.startswith("$"):
        current_object = os.getenv(current_object[1:])

    return current_object
