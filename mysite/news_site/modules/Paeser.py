from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
import json
import lxml


def get_html(url):
    response = requests.get(url)
    return response.text


def get_hype_rate(link, html):
    try:
        res = json.loads(html)
    except ValueError:
        return 0
    num = res['xids'][link]
    return num


def get_all_links(url, html, date):
    news = []
    url_get = 'https://c.rambler.ru/api/app/126/comments-count?xid='
    soup = BeautifulSoup(html, "lxml")
    headers = soup.find_all('a', href=re.compile("^/news/"+date+"/"))
    for head, tag in enumerate(headers):
        blok = []
        link = tag.get('href')
        full_link = url+link
        blok.append(full_link)
        blok.append(headers[head].get_text().replace(u'\xa0', u' '))
        try:
            blok.append(get_hype_rate(full_link, get_html(url_get + full_link)))
        except:
            blok.append('0')
        news.append(blok)
    return news


def main():
    now = datetime.now()
    date = now.strftime("%Y/%m/%d")
    url = "https://lenta.ru"
    url_full = url + "/news/" + date
    return get_all_links(url, get_html(url_full), date)


if __name__ == '__main__':
    main()