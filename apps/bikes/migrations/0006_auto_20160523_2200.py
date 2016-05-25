# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0005_category_short_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.DecimalField(verbose_name='Tarif \xe0 la journ\xe9e', max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
