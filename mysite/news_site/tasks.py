from celery.schedules import crontab
from celery import Celery
from .modules.rss_parser import main as Pars
from .models import News, CustomUser, UrlsTable
from celery import shared_task
from celery.schedules import crontab


from django_celery_beat.models import PeriodicTask, PeriodicTasks, IntervalSchedule


# celery_app = Celery('mysite')


'''schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
#  IntervalSchedule.PERIOD_CHOICES  -  Позволить прльзорвателю настраивать интервалы парсинга

PeriodicTask.objects.create(
    interval=schedule,                  # Рассписание, определённое выше
    name='News_parsing',          # Описание задачи
    task='tests.test',  # Имя задачи
)'''


'''
@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    print('lol')
    # Calls test() every 100 seconds.
    sender.add_periodic_task(100.0, test.s(), name='add-every-10-seconds')
'''


@shared_task(name="test")
def test():
    print('lol')
    urls = [url for url in UrlsTable.objects.all().values_list('url', flat=True)]
    for url in urls:
        for n in Pars(url):
            s = News(news_text=n[0], news_url=n[1], news_hype_rate=0, pub_date=n[2], site_url=url)
            s.save()
