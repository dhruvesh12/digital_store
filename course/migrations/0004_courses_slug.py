# Generated by Django 2.2.4 on 2019-09-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190924_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
