import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Binance.settings')

app = Celery('Binance')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_30s': {
        'task': 'market.tasks.get_coins_data',
        'schedule': 20.0
    }
}

app.autodiscover_tasks()

