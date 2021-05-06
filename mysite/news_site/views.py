import requests
from django.shortcuts import render
from django.views import generic

from .models import News, UrlsTable, CustomUser, UrlsForCategory
from django_celery_beat.models import PeriodicTask

from .charts import DemoChart

from .forms import UserProfileForm, UserRegistrationForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


import pickle

MAX_NEWS_PER_PAGE = 200

user_interest = []


def base_view(request, category, category_number, view):
    num_visits = request.session.get(view, 0)
    request.session[view] = num_visits + 1
    request.session.save()
    if request.user.is_authenticated:
        user_category = UrlsForCategory.objects.all().filter(user=request.user, category=category_number)
        id_request = [url for url in user_category.values_list("url", flat=True)]
        user_urls_values = list(UrlsTable.objects.all().filter(id__in=id_request).values_list("url", flat=True))
        # uuv = [user_urls_values[i - 1] for i in id_request]
        news_list = News.objects.filter(
            site_url__url__in=user_urls_values,
            category__category__exact=category
        )
    else:
        news_list = News.objects.filter(
            category__category__exact=category
        )
        user_urls_values = UrlsTable.objects.all()
        # uuv = user_urls_values


    # order_list = {obj.pk: obj for obj in news_list.site_url.url}
    # objects_ordered = [order_list[pk] for pk in uuv]

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
         'urls_list': user_urls_values,
         'urls': UrlsTable.objects.all(),
         },
    )


class News1(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Политика', 1, 'num_visits1')


class News2(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Экономика', 2, 'num_visits2')



class News3(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Техника', 3, 'num_visits3')


class News4(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Наука', 4, 'num_visits4')


class News5(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Спорт', 5, 'num_visits5')


class News6(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Развлечения', 6, 'num_visits6')


class News7(generic.ListView):
    news = News

    def get(self, request):
        return base_view(request, 'Прочее', 7, 'num_visits7')


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
        user_urls_pol = UrlsForCategory.objects.all().filter(user=self.request.user, category=1)
        user_urls_econ = UrlsForCategory.objects.all().filter(user=self.request.user, category=2)
        user_urls_tech = UrlsForCategory.objects.all().filter(user=self.request.user, category=3)
        user_urls_sci = UrlsForCategory.objects.all().filter(user=self.request.user, category=4)
        user_urls_sport = UrlsForCategory.objects.all().filter(user=self.request.user, category=5)
        user_urls_entr = UrlsForCategory.objects.all().filter(user=self.request.user, category=6)
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

        context = {
            'user_urls': user_urls,
            'user_urls_pol': user_urls_pol,
            'user_urls_econ': user_urls_econ,
            'user_urls_tech': user_urls_tech,
            'user_urls_sci': user_urls_sci,
            'user_urls_sport': user_urls_sport,
            'user_urls_entr': user_urls_entr,
            'urls': UrlsTable.objects.all(),
            'form': form,
        }
        return context


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
