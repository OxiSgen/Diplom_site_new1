# Generated by Django 3.2 on 2021-05-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0016_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='same_news',
            field=models.ManyToManyField(to='news_site.News', verbose_name='Same News'),
        ),
    ]
