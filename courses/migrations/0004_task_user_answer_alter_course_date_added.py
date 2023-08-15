# Generated by Django 4.0.3 on 2022-04-12 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_date_added_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_answer',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 12, 12, 22, 36, 300056, tzinfo=utc), verbose_name='date added course'),
        ),
    ]
