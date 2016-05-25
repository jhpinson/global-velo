# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Titre de la page', max_length=255, verbose_name='Titre')),
                ('subtitle', models.CharField(help_text='Deuxi\xe8me ligne du texte', max_length=255, null=True, verbose_name='Sous-titre', blank=True)),
                ('texte', models.TextField(max_length=1024, null=True, verbose_name='Texte', blank=True)),
                ('url', models.CharField(help_text='Adresse de la page de destination (quand on clique sur le slide)', max_length=255, verbose_name='URL')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('template', models.CharField(default='default', max_length=20, choices=[('default', 'Par d\xe9faut'), ('partners', 'Affichage des partenaires'), ('contacts', 'Affichage du formulaire de contact')])),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='slides/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='Libell\xe9')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='section',
            field=models.ForeignKey(verbose_name='Section', to='pages.Section'),
            preserve_default=True,
        ),
    ]
