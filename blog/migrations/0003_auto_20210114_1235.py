# Generated by Django 3.1.5 on 2021-01-14 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210114_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 14, 7, 35, 1, 161420, tzinfo=utc)),
        ),
    ]
