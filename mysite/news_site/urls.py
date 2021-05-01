from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'', views.Akak.as_view()),
    re_path(r'news1/', views.News1.as_view(), name='News1'),
    re_path(r'news2/', views.News2.as_view(), name='News2'),
    re_path(r'news3/', views.News3.as_view(), name='News3'),
    re_path(r'news4/', views.News4.as_view(), name='News4'),
    re_path(r'news5/', views.News5.as_view(), name='News5'),
    re_path(r'news6/', views.News6.as_view(), name='News6'),
    re_path(r'news7/', views.News7.as_view(), name='News7'),
    re_path(r'newsIndividual/', views.NewsIndividual.as_view(), name='NewsIndividual'),
    re_path(r'unregistered/', views.Unregistered.as_view(), name='Not_logged'),
    re_path(r'profile/', views.UserProfile.as_view(), name='Profile'),
]