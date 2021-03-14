import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carzone.settings')

local_broker = 'amqp://myrabbit:5672'
app = Celery('myshop', broker=local_broker)

app.autodiscover_tasks()
