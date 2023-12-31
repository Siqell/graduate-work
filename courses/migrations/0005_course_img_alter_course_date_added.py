# Generated by Django 4.0.3 on 2022-04-17 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_task_user_answer_alter_course_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.CharField(default='#565687', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 10, 33, 41, 552716, tzinfo=utc), verbose_name='date added course'),
        ),
    ]
