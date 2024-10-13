import atexit
import importlib
import pkgutil

from apscheduler.schedulers.background import BackgroundScheduler

_scheduler = BackgroundScheduler()

job = _scheduler.scheduled_job


def start_jobs():
    _scheduler.start()
    atexit.register(lambda: _scheduler.shutdown())

    for submodule in pkgutil.iter_modules(__path__):
        importlib.import_module("." + submodule.name, __name__)
