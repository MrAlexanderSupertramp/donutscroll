# Generated by Django 3.0.4 on 2020-07-15 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_auto_20200712_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='catid',
        ),
    ]
