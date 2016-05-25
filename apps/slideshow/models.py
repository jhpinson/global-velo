# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from sorl.thumbnail.fields import ImageField

class Slide(models.Model):

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"

    title = models.CharField('Titre', max_length=255, help_text='Première ligne du texte')
    subtitle = models.CharField('Sous-titre', max_length=255, help_text='Deuxième ligne du texte', null=True, blank=True)
    description = models.TextField('Description', max_length=1024, help_text='Description courte', null=True, blank=True)
    url = models.CharField('URL', max_length=255, help_text='Adresse de la page de destination (quand on clique sur le slide)')
    visible = models.BooleanField(verbose_name="Visible", default=True)

    picture = ImageField('Photo', upload_to='slides/')

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains","subtitle__icontains",)