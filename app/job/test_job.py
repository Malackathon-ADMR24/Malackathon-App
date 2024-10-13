import time

from . import job


@job(trigger='interval', minutes=1)  # se ejecuta cada 1 minuto
def test_job_1():
    print("Test interval job:", time.strftime("%H:%M:%S"))


@job(trigger='cron', hour=17, minute=31, second=0)  # se ejecuta todos los días a las 17:31:00
def test_job_2():
    print("Test cron job:", time.strftime("%H:%M:%S"))
