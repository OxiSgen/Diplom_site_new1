from bs4 import BeautifulSoup
import requests
import re


def soup_getter(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    if page.status_code == 200:
        return soup


def get_hype_rate_for_ria(url):
        base = 'https://ria.ru/services/dynamics/'
        hype = []
        js_parts_url = base + ''.join(re.findall(r'\b[0-9]{8}\b', url)) + '/' + \
                       ''.join(re.findall(r'[0-9]{10}', url)) + '.html'
        soup = soup_getter(js_parts_url)
        for elem in soup.find_all('span', class_='m-value'):
            hype.append(elem.text)
        # comment = soup.find_all('a', class_='js__toggle-chat-article color-bg-hover')
        # hype.append(comment.find_all)
        return hype[:-8:-1]