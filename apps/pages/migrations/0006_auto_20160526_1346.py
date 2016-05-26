# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='texte',
            field=models.TextField(null=True, verbose_name='Texte', blank=True),
            preserve_default=True,
        ),
    ]
