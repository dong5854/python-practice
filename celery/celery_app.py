import celeryconfig
from celery import Celery

app = Celery()
app.config_from_object(celeryconfig)

if __name__ == "main":
    app.start()
