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


@shared_task(name="test")
def test():
    '''urls = [url for url in UrlsTable.objects.all().values_list('url', flat=True)]
    print(urls)
    for url in urls:
        for n in Pars(url):
            # MZ = tz.gettz('Europe/Moscow')
            # date = parse(n[2]).strftime("%Y-%m-%d %H:%M:%S")
            s = News(news_text=n[0],
                     news_url=n[1],
                     news_hype_rate=0,
                     pub_date=n[2],
                     site_url=UrlsTable.objects.get(url__exact=url)
                     )
            s.save()'''
    # News.objects.all().delete()
    '''for x, str in enumerate(News.objects.all().values_list("news_text", flat=True)):
        for y, str2 in enumerate(News.objects.all()):
            if str != str2:
                if fuzz.token_set_ratio(str, str2) > 59:
                    News.objects.get(news_text=str).news_set.add(News.objects.get(news_text=str2))
            else:
                continue'''

                # if sites[str[1]] > sites[str2[1]]:
                    # del str_list[x]
                # else:
                    # del str_list[y]
                # print(x, y, fuzz.token_set_ratio(str[0], str2[0]), str[0], str[1], '-/-', str2[0], str2[1])