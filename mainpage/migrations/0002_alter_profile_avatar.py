# Generated by Django 4.0.3 on 2022-05-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='defaultAvatar.jpg', upload_to='image/avatars/'),
        ),
    ]
