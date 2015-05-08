# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import sorl.thumbnail.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=128, verbose_name='Nom')),
                ('description', models.CharField(max_length=512, verbose_name='Description')),
                ('website', models.URLField(max_length=1024, null=True, verbose_name='Site internet', blank=True)),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='num\xe9ro de t\xe9l\xe9phone', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Adresse email', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Afficher ce partenaire sur le site')),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='partners/', null=True, verbose_name='Logo', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
