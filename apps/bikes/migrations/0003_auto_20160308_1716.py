# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_auto_20150328_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bike',
            options={'verbose_name': 'V\xe9lo', 'verbose_name_plural': 'V\xe9los'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Cat\xe9gorie', 'verbose_name_plural': 'Cat\xe9gories'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Taille', 'verbose_name_plural': 'Tailles'},
        ),
    ]
