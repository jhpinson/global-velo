# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AlterField(
            model_name='page',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Sous-titre', blank=True),
            preserve_default=True,
        ),
    ]
