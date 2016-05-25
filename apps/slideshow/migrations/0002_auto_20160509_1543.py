# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='description',
            field=models.TextField(default='', help_text='Description courte', max_length=1024, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle',
            field=models.CharField(help_text='Deuxi\xe8me ligne du texte', max_length=255, verbose_name='Sous-titre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(help_text='Premi\xe8re ligne du texte', max_length=255, verbose_name='Titre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='url',
            field=models.CharField(help_text='Adresse de la page de destination (quand on clique sur le slide)', max_length=255, verbose_name='URL'),
            preserve_default=True,
        ),
    ]
