# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from sorl.thumbnail.fields import ImageField

class Section(models.Model):

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    title = models.CharField('Libellé', max_length=64)

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

class Page(models.Model):

    PAGE_TEMPLATES_CHOICES = (
        ('default', 'Par défaut'),
        ('partners', 'Affichage des partenaires'),
        ('contacts', 'Affichage du formulaire de contact')
        )

    

    class Meta:
        ordering = ['order',]
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    section = models.ForeignKey(Section, verbose_name="Section")
    title = models.CharField('Titre', max_length=255, help_text='Titre de la page')
    subtitle = models.CharField('Sous-titre', max_length=255, help_text='', null=True, blank=True)
    texte = models.TextField('Texte', help_text='', null=True, blank=True)

    order = models.PositiveSmallIntegerField(verbose_name='Ordre', help_text='', blank=True, null = True)
    
    visible = models.BooleanField(verbose_name="Visible", default=True)
    template = models.CharField(max_length=20,choices=PAGE_TEMPLATES_CHOICES, default='default')

    picture = ImageField('Photo', upload_to='slides/', null=True, blank=True)
    image = ImageField('Image', upload_to='pages/', null=True, blank=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains","subtitle__icontains",)