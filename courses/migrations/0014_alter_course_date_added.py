# Generated by Django 4.0.3 on 2022-05-31 11:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_date_added_alter_course_file_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 11, 53, 15, 777562, tzinfo=utc), verbose_name='date added course'),
        ),
    ]
