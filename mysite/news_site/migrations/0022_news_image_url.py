# Generated by Django 3.2 on 2021-05-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0021_alter_news_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
