# Generated by Django 2.2.4 on 2019-09-24 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='thumnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/courses_image/'),
            preserve_default=False,
        ),
    ]