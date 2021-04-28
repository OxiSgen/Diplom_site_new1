from django.urls import path

from . import views

urlpatterns = [
    path('', views.News1.as_view(), name='News1'),
    path('news2/', views.News2.as_view(), name='News2'),
    path('news3/', views.News3.as_view(), name='News3'),
    path('news4/', views.News4.as_view(), name='News4'),
    path('news5/', views.News5.as_view(), name='News5'),
    path('news6/', views.News6.as_view(), name='News6'),
    path('news7/', views.News7.as_view(), name='News7'),
    path('newsIndividual/', views.NewsIndividual.as_view(), name='NewsIndividual'),
    path('unregistered/', views.Unregistered.as_view(), name='Not_logged'),
    path('profile/', views.UserProfile.as_view(), name='Profile'),
]