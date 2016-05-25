# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Sous-titre')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='slides/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
            bases=(models.Model,),
        ),
    ]
