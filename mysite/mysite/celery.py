from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

celery_app = Celery('mysite')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
