# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20160523_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order'], 'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Ordre', blank=True),
            preserve_default=True,
        ),
    ]
