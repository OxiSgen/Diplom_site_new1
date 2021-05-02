from django.db import models
from django.contrib.auth.models import AbstractUser
from django_celery_beat.models import PeriodicTask


# Create your models here.


class UrlsTable(models.Model):
    url = models.CharField(max_length=200, null=False, blank=False)
    site_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.url


class CustomUser(AbstractUser):
    text = models.CharField(max_length=2000, null=True, blank=True)
    # task = models.ManyToManyField(PeriodicTask)
    urls = models.ManyToManyField(UrlsTable, through='PriorityForUser')


class PriorityForUser(models.Model):
    url = models.ForeignKey(UrlsTable, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prior = models.IntegerField(blank=True, null=True)


class News(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    news_text = models.CharField(max_length=200, blank=True, null=True)
    news_url = models.CharField(max_length=200, blank=True, null=True)
    site_url = models.ForeignKey(UrlsTable, on_delete=models.CASCADE, blank=True, null=True)
    news_hype_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    same_news = models.ManyToManyField('self', verbose_name="Same News")  # symmetrical=False для того, чтобы убрать симметрию.

    class Meta:
        ordering = ["news_text"]
