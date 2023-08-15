# Generated by Django 4.0.3 on 2022-05-24 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_course_file_name_remove_course_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 10, 51, 27, 707007, tzinfo=utc), verbose_name='date added course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='file_course',
            field=models.FileField(default='defaultDocxFile', upload_to='docx/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='defaultImage', upload_to='image/'),
        ),
    ]
