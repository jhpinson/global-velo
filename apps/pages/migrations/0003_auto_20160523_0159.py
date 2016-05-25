# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160517_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(upload_to='slides/', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
    ]
