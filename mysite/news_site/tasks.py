from celery.schedules import crontab
from celery import Celery
from .modules.rss_parser import main as Pars
from .models import News, CustomUser, UrlsTable, Category
from celery import shared_task
from celery.schedules import crontab
from dateutil.parser import parse
from dateutil import tz
from fuzzywuzzy import fuzz
import datetime
import pytz
from django.db import IntegrityError
import fasttext
from .modules.Hype_Rate import *

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


cat_to_cat_transform = {
    'society': 'Политика',
    'economy': 'Экономика',
    'technology': 'Техника',
    'science': 'Наука',
    'sports': 'Спорт',
    'entertainment': 'Развлечения',
    'other': 'Прочее',
    'not_news': 'Прочее',
}


class CategoryChecker:
    def __init__(self):
        self.model = fasttext.load_model('news_site/news_categorization_model/ru_cat_v5.ftz')

    def determine_category(self, text):
        label_tuple = self.model.predict(text)
        prediction = label_tuple[0][0].replace('__label__', '')
        return prediction


def f(li):
    temp = {i[0]: i[1:] for i in li}
    arr = []
    for key, value in temp.items():
        value.insert(0, key)
        arr.append(value)
    return arr


@shared_task(name="clear_db")
def delete_old_news():
    News.objects.all().delete()
    test()


@shared_task(name="test")
def test():
    '''urls = [url for url in UrlsTable.objects.all().values_list('url', flat=True)]
    ch = CategoryChecker()
    for url in urls:
        for n in f(Pars(url)):
            if int("{:%s}".format(datetime.datetime.now(pytz.timezone('Europe/Moscow')))) - int("{:%s}".format(n[2])) < 1209600:
                #  print(n[0], ch.determine_category(n[0]))
                try:
                    str = n[0]
                    if "ria.ru" in url:
                        try:
                            hype = sum(map(int, get_hype_rate_for_ria(n[1])))
                        except:
                            hype = 0
                    else:
                        hype = 0
                    category = ch.determine_category(n[0])
                    s = News(news_text=str,
                             news_url=n[1],
                             news_hype_rate=hype,
                             pub_date=n[2].strftime("%Y-%m-%d %H:%M"),
                             site_url=UrlsTable.objects.get(url__exact=url),
                             image_url=n[3],
                             category=Category.objects.get(category__exact=cat_to_cat_transform[category])
                             )
                    s.save()
                    for y, str2 in enumerate(News.objects.all().values_list("news_text", flat=True)):
                        if str == str2:
                            continue
                        if fuzz.token_set_ratio(str, str2) > 59:
                            n = News.objects.get(news_text=str)
                            n.same_news.add(News.objects.get(news_text=str2))
                            News.save(n)
                except IntegrityError:
                    continue'''
