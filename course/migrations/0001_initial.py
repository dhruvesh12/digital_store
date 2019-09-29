# Generated by Django 2.2.4 on 2019-09-17 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('objective', models.TextField(blank=True, null=True)),
                ('requriment', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.category')),
            ],
        ),
    ]
