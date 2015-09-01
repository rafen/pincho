from __future__ import absolute_import
import Adafruit_DHT
from celery import task
from button.models import Temp


@task(name='button.tasks.temp')
def temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    if humidity and temperature:
        Temp.objects.create(temp=temperature, humidity=humidity)
    return humidity, temperature


@task(name='button.tasks.test')
def test(param):
    return 'The test task executed with argument "%s" ' % param
