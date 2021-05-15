# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.views import generic

from .models import News, UrlsTable, CustomUser, UrlsForCategory
from django_celery_beat.models import PeriodicTask

from .charts import DemoChart

from .forms import UserProfileForm, UserRegistrationForm, UserTagsForm
'''UserTagsForm'''

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import numpy as np

import json

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.forms.models import model_to_dict

from django.core import serializers

import datetime


import pickle

MAX_NEWS_PER_PAGE = 200

user_interest = []


def base_view(request, category, category_number, view, filter_string='', order="-pub_date", flagHot=0, flag_date=False):
    num_visits = request.session.get(view, 0)
    request.session[view] = num_visits + 1
    request.session.save()
    result = []
    if request.user.is_authenticated:
        user_category = UrlsForCategory.objects.all().filter(user=request.user, category=category_number)
        id_request = [url for url in user_category.values_list("url", flat=True)]
        user_urls_values = list(UrlsTable.objects.all().filter(id__in=id_request).values_list("url", flat=True))
        if not flagHot:
            if not flag_date:
                news_list = News.objects.filter(
                    site_url__url__in=user_urls_values,
                    category__category__exact=category,
                    news_text__icontains=filter_string
                ).order_by(order)
            else:
                date = filter_string.split('-')
                news_list = News.objects.filter(
                    site_url__url__in=user_urls_values,
                    category__category__exact=category,
                    pub_date__year=date[0],
                    pub_date__month=date[1],
                    pub_date__day=date[2],
                ).order_by(order)
        elif flagHot == 1:
            if not flag_date:
                news_list = News.objects.filter(
                    site_url__url__in=user_urls_values,
                    news_hype_rate__gte=50,
                    news_text__icontains=filter_string
                ).order_by(order)
            else:
                date = filter_string.split('-')
                news_list = News.objects.filter(
                    site_url__url__in=user_urls_values,
                    news_hype_rate__gte=50,
                    pub_date__year=date[0],
                    pub_date__month=date[1],
                    pub_date__day=date[2],
                ).order_by(order)
        else:
            curuser = CustomUser.objects.get(pk=request.user.id).user_tags
            q = Q()
            tags = json.loads(curuser)
            print(tags)
            #  tags.append(filter_string)
            for tag in tags:
                q |= Q(news_text__icontains=tag)
            news_list = News.objects.filter(
                q,
                site_url__url__in=user_urls_values,
            ).order_by(order)
        if len(id_request) > 1:
            uuv = [user_urls_values[i - min(id_request)] for i in id_request]
            sortkey = {j: i for i, j in enumerate(uuv)}
            split_arr = np.array_split(news_list, 50)
            for arr in split_arr:
                result += sorted(arr, key=lambda r: sortkey[r.site_url.url])
            result = np.array(result).flatten()
        else:
            result = news_list
    else:
        result = News.objects.filter(
            category__category__exact=category
        ).order_by('-pub_date')
        user_urls_values = UrlsTable.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(result, 18)
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
         'urls_list': user_urls_values,
         'urls': UrlsTable.objects.all(),
         },
    )


class News1(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Политика', 1, 'num_visits1', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Политика', 1, 'num_visits1', text)
        except:
            return base_view(request, 'Политика', 1, 'num_visits1')


class News2(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Экономика', 2, 'num_visits2', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Экономика', 2, 'num_visits2', text)
        except:
            return base_view(request, 'Экономика', 2, 'num_visits2')


class News3(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Техника', 3, 'num_visits3', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Техника', 3, 'num_visits3', text)
        except:
            return base_view(request, 'Техника', 3, 'num_visits3')


class News4(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Наука', 4, 'num_visits4', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Наука', 4, 'num_visits4', text)
        except:
            return base_view(request, 'Наука', 4, 'num_visits4')


class News5(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Спорт', 5, 'num_visits5', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Спорт', 5, 'num_visits5', text)
        except:
            return base_view(request, 'Спорт', 5, 'num_visits5')


class News6(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Развлечения', 6, 'num_visits6', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Развлечения', 6, 'num_visits6', text)
        except:
            return base_view(request, 'Развлечения', 6, 'num_visits6')


class News7(generic.ListView):
    news = News

    def get(self, request):
        try:
            text = self.request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, 'Прочее', 7, 'num_visits7', text, flag_date=True)
            except ValueError:
                return base_view(request, 'Прочее', 7, 'num_visits7', text)
        except:
            return base_view(request, 'Прочее', 7, 'num_visits7')


'''class NewsIndividual(generic.TemplateView):
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
        return context'''


class NewsIndividual(generic.TemplateView):
    template_name = 'news_site/individual.html'

    def get(self, request):
        '''curuser = CustomUser.objects.get(pk=self.request.user.id)
        curuser.user_tags = json.dumps([u'Лукашенко', u'Байден', u'Вашингтон', u'Путин', u'Война'], ensure_ascii=False)
        curuser.save()'''
        '''
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
        }'''
        try:
            text = self.request.GET.get('search')
            return base_view(request, '', 7, 'num_visits7', text, flagHot=2)
        except:
            return base_view(request, '', 7, 'num_visits7', flagHot=2)


class NewsHot(generic.TemplateView):
    template_name = 'news_site/individual.html'

    def get(self, request):
        # context = super().get_context_data(**kwargs)
        try:
            text = request.GET.get('search')
            try:
                datetime.datetime.strptime(text, '%Y-%m-%d')
                return base_view(request, '', 7, 'num_visits7', text, order="-news_hype_rate", flagHot=1, flag_date=True)
            except ValueError:
                return base_view(request, '', 7, 'num_visits7', text, order="-news_hype_rate", flagHot=1)
        except:
            return base_view(request, '', 7, 'num_visits7', order="-news_hype_rate", flagHot=1)


'''class UserProfile(generic.FormView):
    template_name = 'news_site/profile.html'

    def get_context_data(self, **kwargs):
        # context = super(UserProfile, self).get_context_data(**kwargs)
        curuser = CustomUser.objects.get(pk=self.request.user.id)

        context = {
            'user_urls': UrlsForCategory.objects.all().filter(user=self.request.user),
            'user_urls_pol': UrlsForCategory.objects.all().filter(user=self.request.user, category=1),
            'user_urls_econ': UrlsForCategory.objects.all().filter(user=self.request.user, category=2),
            'user_urls_tech': UrlsForCategory.objects.all().filter(user=self.request.user, category=3),
            'user_urls_sci': UrlsForCategory.objects.all().filter(user=self.request.user, category=4),
            'user_urls_sport': UrlsForCategory.objects.all().filter(user=self.request.user, category=5),
            'user_urls_entr': UrlsForCategory.objects.all().filter(user=self.request.user, category=6),
            'urls': UrlsTable.objects.all(),
            'form_tag': UserTagsForm(instance=curuser),
        }
        return context

    def post(self, request, *args, **kwargs):
        user_urls = UrlsForCategory.objects.all().filter(user=self.request.user)

        if self.request.method == 'POST' and 'save' in self.request.POST:
            form = UserProfileForm(initial={
                'all_urls': [
                    url for url in user_urls.values_list("url", flat=True)
                ]
            })
        if self.request.method == 'POST' and 'sv-tag' in self.request.POST:
            form_tag = UserTagsForm(self.request.POST)
            if form_tag.is_valid():
                print(form_tag.user_tags)
                instance = form_tag.save()
        else:
            curuser = CustomUser.objects.get(pk=self.request.user.id)
            form_tag = UserTagsForm(instance=curuser)

        return render(request, self.template_name, {'form_tag': form_tag})'''


def _get_form(request, form_name, prefix):
    data = request.POST if prefix in request.POST else None
    return form_name(data, prefix=prefix)


class UserProfile(generic.TemplateView):
    template_name = 'news_site/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        curuser = CustomUser.objects.get(pk=self.request.user.id)
        context['form'] = UserProfileForm(
            data=self.request.POST if 'save' in self.request.POST else None,
        )
        context['form_tag'] = UserTagsForm(
            instance = curuser,
            data = self.request.POST if 'sv-tag' in self.request.POST else None,
        )
        context['user_urls'] = UrlsForCategory.objects.all().filter(user=self.request.user)
        context['user_urls_pol'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=1)
        context['user_urls_econ'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=2)
        context['user_urls_tech'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=3)
        context['user_urls_sci'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=4)
        context['user_urls_sport'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=5)
        context['user_urls_entr'] = UrlsForCategory.objects.all().filter(user=self.request.user, category=6)
        context['urls'] = UrlsTable.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if context['form'].is_valid():
            '''instance = context['form'].save()
            render(request, context, instance.pk)'''
            pass

        elif context['form_tag'].is_valid():
            instance = context['form_tag'].save(commit=False)
            instance.user_tags = request.POST['user_tags']
            instance.save()

        else:
            render('Error(s) encountered during form processing, please review below and re-submit')

        return self.render_to_response(context)





class Unregistered(generic.TemplateView):
    template_name = 'news_site/unregistered.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


'''if self.request.method == 'POST':
    user_form = UserTagsForm(self.request.POST)
    if user_form.is_valid():
        curuser = CustomUser.objects.get(pk=self.request.user.id)
        curuser.user_tags = json.dumps(str(user_form.parse_data).split(','))
        curuser.save()
        return render(self.request, 'profile.html', {'user_form': user_form})
else:
    user_form = UserRegistrationForm()
return render(self.request, 'profile.html', {'user_form': user_form})'''
