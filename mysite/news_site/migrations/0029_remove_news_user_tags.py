# Generated by Django 3.2.1 on 2021-05-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0028_auto_20210507_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='user_tags',
        ),
    ]
