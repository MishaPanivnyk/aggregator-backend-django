# Generated by Django 4.1.13 on 2024-03-07 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=60)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('time_create', models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 7, 16, 28, 24, 458426))),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
