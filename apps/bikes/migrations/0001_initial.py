# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=64, verbose_name='Nom du v\xe9lo')),
                ('description', models.TextField(max_length=1024, verbose_name='Description')),
                ('price', models.DecimalField(verbose_name='Tarif \xe0 la journ\xe9e', max_digits=5, decimal_places=2)),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='bikes/', verbose_name='Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=64, verbose_name='Libell\xe9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bike',
            name='sizes',
            field=models.ManyToManyField(to='bikes.Size', verbose_name='Tailles disponibles'),
            preserve_default=True,
        ),
    ]
