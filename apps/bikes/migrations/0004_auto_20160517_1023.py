# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_auto_20160308_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Marque',
                'verbose_name_plural': 'Marques',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(verbose_name='Marque', blank=True, to='bikes.Brand', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='for_sale',
            field=models.BooleanField(default=True, help_text='D\xe9cocher la case pour mettre le v\xe9lo dans l\u2019offre location', verbose_name='\xc0 vendre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='gender',
            field=models.CharField(default='man', max_length=20, choices=[('man', 'Homme'), ('woman', 'Femme'), ('child', 'Enfant')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='second_hand',
            field=models.BooleanField(default=False, verbose_name='V\xe9lo d\u2019occasion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bike',
            name='label',
            field=models.CharField(max_length=64, verbose_name='Nom du mod\xe8le du v\xe9lo'),
            preserve_default=True,
        ),
    ]
