# Generated by Django 4.0.3 on 2022-06-01 15:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_course_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 15, 3, 30, 238652, tzinfo=utc), verbose_name='date added course'),
        ),
    ]