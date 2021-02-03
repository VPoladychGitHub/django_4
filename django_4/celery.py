import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_4.settings')

app = Celery('django_4')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
app.conf.beat_schedule = {
    # выполняется каждую минуту
    # 'scraping-task-one-min': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab()
    # },
    'parsing': {
        'task': 'triangle.tasks.parse_quoters',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request88: {self.request!r}')
