# Generated by Django 4.0.3 on 2022-04-10 16:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_course_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 16, 38, 20, 167785, tzinfo=utc), verbose_name='date added course'),
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]