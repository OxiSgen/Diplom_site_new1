from celery.schedules import crontab
from celery import Celery
from .modules.rss_parser import main as Pars
from .models import News, CustomUser, UrlsTable
from celery import shared_task
from celery.schedules import crontab
from dateutil.parser import parse
from dateutil import tz
from fuzzywuzzy import fuzz


from django_celery_beat.models import PeriodicTask, PeriodicTasks, IntervalSchedule


'''schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
#  IntervalSchedule.PERIOD_CHOICES  -  Позволить прльзорвателю настраивать интервалы парсинга

PeriodicTask.objects.create(
    interval=schedule,                  # Рассписание, определённое выше
    name='News_parsing',          # Описание задачи
    task='test',  # Имя задачи
)'''


def f(li):
    temp = {i[0]: i[1:] for i in li}
    print(temp)
    print(temp)
    arr = []
    for key, value in temp.items():
        value.insert(0, key)
        arr.append(value)
    return arr


@shared_task(name="test")
def test():
    '''urls = [url for url in UrlsTable.objects.all().values_list('url', flat=True)]
    print(urls)
    for url in urls:
        for n in f(Pars(url)):
            if int("{:%s}".format(datetime.datetime.now(pytz.timezone('Europe/Moscow')))) - int("{:%s}".format(n[2])) < 604800:
                try:
                    s = News(news_text=n[0],
                             news_url=n[1],
                             news_hype_rate=0,
                             pub_date=n[2].strftime("%Y-%m-%d %H:%M"),
                             site_url=UrlsTable.objects.get(url__exact=url),
                             image_url=n[3],
                             )
                    s.save()
                except IntegrityError:
                    pass'''

    '''for x, str in enumerate(News.objects.all().values_list("news_text", flat=True)):
        for y, str2 in enumerate(News.objects.all().values_list("news_text", flat=True)):
            if x != y:
                if fuzz.token_set_ratio(str, str2) > 59:
                    n = News.objects.get(news_text=str)
                    n.same_news.add(News.objects.get(news_text=str2))
                    News.save(n)
            else:
                continue'''       
