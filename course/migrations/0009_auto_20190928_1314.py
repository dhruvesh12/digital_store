# Generated by Django 2.2.4 on 2019-09-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.TextField(max_length=200),
        ),
    ]