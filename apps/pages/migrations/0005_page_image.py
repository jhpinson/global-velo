# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160523_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='pages/', null=True, verbose_name='Image', blank=True),
            preserve_default=True,
        ),
    ]
