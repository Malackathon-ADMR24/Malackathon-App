import yaml

DEFAULT_CONFIGURATION_FILEPATH = "configuration.yml"

_configuration_object = {}


def load_configuration(filepath: str):
    global _configuration_object
    with open(filepath) as fh:
        _configuration_object = yaml.safe_load(fh)


def config(path):
    current_object = _configuration_object
    steps = path.split(".")
    for step in steps:
        current_object = current_object[step]
    return current_object
