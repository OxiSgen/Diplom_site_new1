import requests
from django.shortcuts import render
from django.views import generic

from .models import News, UrlsTable, CustomUser, UrlsForCategory
from django_celery_beat.models import PeriodicTask

from .charts import DemoChart

from .forms import UserProfileForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


import pickle

user_interest = []


class News1(generic.ListView):
    news = News

    def get(self, request):
        num_visits1 = request.session.get('num_visits1', 0)
        request.session['num_visits1'] = num_visits1 + 1
        request.session.save()
        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=1)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values), category__category__exact='Политика')
            print(news_list)
        else:
            news_list = News.objects.filter(category__category__exact='Политика')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News2(generic.ListView):
    news = News

    def get(self, request):
        num_visits2 = request.session.get('num_visits2', 0)
        request.session['num_visits2'] = num_visits2 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=2)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Экономика')
        else:
            news_list = News.objects.filter(category__category__exact='Экономика')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News3(generic.ListView):
    news = News

    def get(self, request):
        num_visits3 = request.session.get('num_visits3', 0)
        request.session['num_visits3'] = num_visits3 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=3)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Техника')
        else:
            news_list = News.objects.filter(category__category__exact='Техника')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News4(generic.ListView):
    news = News

    def get(self, request):
        num_visits4 = request.session.get('num_visits4', 0)
        request.session['num_visits4'] = num_visits4 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=4)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Наука')
        else:
            news_list = News.objects.filter(category__category__exact='Наука')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News5(generic.ListView):
    news = News

    def get(self, request):
        num_visits5 = request.session.get('num_visits5', 0)
        request.session['num_visits5'] = num_visits5 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=5)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Спорт')
        else:
            news_list = News.objects.filter(category__category__exact='Спорт')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News6(generic.ListView):
    news = News

    def get(self, request):
        num_visits6 = request.session.get('num_visits6', 0)
        request.session['num_visits6'] = num_visits6 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=6)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Развлечения')
        else:
            news_list = News.objects.filter(category__category__exact='Развлечения')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class News7(generic.ListView):
    news = News

    def get(self, request):
        num_visits7 = request.session.get('num_visits7', 0)
        request.session['num_visits7'] = num_visits7 + 1
        request.session.save()

        if request.user.is_authenticated:
            user_category = UrlsForCategory.objects.all().filter(user=self.request.user, category=7)
            id_request = [url for url in user_category.values_list("url", flat=True)]
            user_urls_values = UrlsTable.objects.all().filter(
                id__in=id_request
            ).values_list("url", flat=True)
            print(user_urls_values)
            news_list = News.objects.filter(site_url__url__in=list(user_urls_values),
                                            category__category__exact='Прочее')
        else:
            news_list = News.objects.filter(category__category__exact='Прочее')

        page = request.GET.get('page', 1)
        paginator = Paginator(news_list, 18)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': numbers,
             'urls': UrlsTable.objects.all(),
             },
        )


class NewsIndividual(generic.TemplateView):
    template_name = 'news_site/individual.html'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        num_visits8 = self.request.session.get('num_visits8', 0)
        self.request.session['num_visits8'] = num_visits8 + 1
        self.request.session.save()

        # self.request.session.flush()
        periodic_tasks = list(PeriodicTask.objects.all()[1:])

        context = {
            'chart': DemoChart(queryset=list(self.request.session.items())),
            'num_visits': self.request.session.items(),  # num_visits appended
            'periodic': periodic_tasks,
            'urls': UrlsTable.objects.all(),
        }
        return context


class UserProfile(generic.TemplateView):
    template_name = 'news_site/profile.html'

    def get_context_data(self, **kwargs):
        user_urls = UrlsForCategory.objects.all().filter(user=self.request.user)
        if self.request.method == 'POST':
            if "save" in self.request.POST:
                pass
                # form = UserProfileForm(self.request.POST)
                # form.fields['urls'].queryset = PriorityForUser.objects.all().filter(user=self.request.user)
        else:
            form = UserProfileForm(initial={
                'all_urls': [
                    url for url in user_urls.values_list("url", flat=True)
                ]
            })
            form1 = UserProfileForm(initial={
                'all_urls': [
                    url for url in user_urls.values_list("url", flat=True)
                ]
            })

        context = {
            'user_urls': user_urls,
            'urls': UrlsTable.objects.all(),
            'form': form,
            'form1': form1,
        }
        return context


class Unregistered(generic.TemplateView):
    template_name = 'news_site/unregistered.html'
