# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='articles/')),
                ('category', models.ManyToManyField(to='pastime.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pastime.Location')),
            ],
            options={
                'ordering': ['sport_name'],
            },
        ),
    ]