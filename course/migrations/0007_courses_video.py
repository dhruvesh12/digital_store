# Generated by Django 2.2.4 on 2019-09-27 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20190924_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='courses_video/'),
            preserve_default=False,
        ),
    ]
