from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
import requests
import json
import re
import urllib.parse as urlparse
import feedparser
# from Hype_Rate import *


class MyException(BaseException):
    pass


def clear_text(bad_text):
    # Возвращает исправленный текст

    bad_text = str(bad_text)
    return bad_text.replace("&quot;", "\"").replace("&amp;", "&") \
        .replace("&apos;", "'").replace("&gt;", ">").replace("&lt;", "<")


def soup_getter(url):
    # Возвращаем суп по указанному URL

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, "lxml")
    if page.status_code == 200:
        return soup


def rss_feeds_urls(url):
    # функция возвращает массив rss каналов с введёного пользователем url

    try:
        soup = soup_getter(url)
        rss_feeds = []
        try:
            rss_urls = soup.find_all('a', attrs={'href': re.compile(r"rss")})
            for r in rss_urls:
                rss_feeds.append(r.get('href'))
            if not rss_feeds:
                rss_urls = soup.find(lambda tag: tag.name == "a"
                                     and ("rss" in str(tag.text).lower()
                                          or "feeds" in str(tag.text).lower()
                                          )
                                     ).get('href')
                rss_feeds.append(rss_urls)
        except TypeError:
            try:
                rss_urls = soup.find(lambda tag: tag.name == "a"
                                     and ("rss" in str(tag.text).lower()
                                          or "feeds" in str(tag.text).lower()
                                          )
                                     ).get('href')
                rss_feeds.append(rss_urls)
            except TypeError:
                return "Не удалось получить RSS ленту сайта"
        for i, feed in enumerate(rss_feeds):
            if "http" not in feed:
                rss_feeds[i] = urlparse.urljoin(url, feed)
        return rss_feeds
    except BaseException:
        print('У данного новостного ресурса нет RSS ленты. Возможно её не удалось обнаружить.')
        raise MyException()


def is_this_rss(rss_feed):
    # Функция проверки, является ли url rss канал rss каналом

    try:
        d = feedparser.parse(rss_feed).feed.link
        return True
    except AttributeError:
        return False


def rss_text(rss_feed):
    # Функция возвращает текст из rss канала, если это действительно rss канал

    if is_this_rss(rss_feed):
        soup = soup_getter(rss_feed)
        if "&gt;" in str(soup):
            return clear_text(soup)
        else:
            return soup
    else:
        print("Это не rss канал")
        # запускаем поиск rss канала на этой странице
        # (актуально для сайтов типо Дождя и 3Dnews)


def rss_feedparser(rss_url):
    # Парсим RSS канал с помощью библиотеки feedparser
    feed = []
    d = feedparser.parse(rss_url).entries
    for i in d:
        feed.append([i.title, i.link, i.published])
        '''
        print(i.title)  # Заголовок
        print(i.link)  # Ссылка
        print(i.published)  # Дата публикации    
        print(i.tags)  # Теги
        print(i.summary)  # Текст статьи
        '''
        print('\n')
    return feed


def news_for_parsing_html(url):
    # Затычка для HTML поиска
    """
    soupchik = soup_getter(url)
    print(soupchik.find_all('div', class_='cell-list__item m-no-image'))
    """
    pass


def main(url):
    href = url
    rss = rss_feeds_urls(href)
    return rss_feedparser(''.join(rss))

    '''
    try:
        # На дожде под значком RSS скрывается ещё одна страница с выбором лент!!!     +
        # На 3Dnews та же фигня. Нужна дополнительная обработка.                      +
        # Но как понять, RSS лента вернулась или нет?                                 +
        # По расширению не получится, на 3Dnews его нет.                              +

        # Повторный поиск по странице даёт необходимый канал!!!
        # В общем случае можно использовать рекурсию

        # TheWallStreetJournal почему-то не даёт вытащить rss ленту                   +
        # Как выяснилось, у страницы возвращаемый код 403                             +

        # В МК.ру rss лента спрятана в кнопке "подписка"
        # Стоит попробовать сначала исать кнопки "Подписка"
        # и "subscription", чтобы эффективнее искать rss каналы

        # У "Аргументы и факты" вообще в жопе запрятана ссылка...
        # Хотя общая есть и на поверхности

        rss = rss_feeds_urls(href)
        print("Удалось найти следующие rss-каналы")
        for i, r in enumerate(rss):
            feeds[i] = r
        print(feeds, sep='\n')
        

    except MyException:
        print('Затычка для парсинга HTML')
        # news_for_parsing_html(href)
    '''



