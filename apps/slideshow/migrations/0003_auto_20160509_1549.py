# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0002_auto_20160509_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.TextField(help_text='Description courte', max_length=1024, null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle',
            field=models.CharField(help_text='Deuxi\xe8me ligne du texte', max_length=255, null=True, verbose_name='Sous-titre', blank=True),
            preserve_default=True,
        ),
    ]
