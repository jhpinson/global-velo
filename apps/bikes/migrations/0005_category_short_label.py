# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0004_auto_20160517_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='short_label',
            field=models.SlugField(default='', max_length=64, verbose_name='Libell\xe9 raccourci'),
            preserve_default=False,
        ),
    ]
