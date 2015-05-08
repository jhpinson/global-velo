# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from sorl.thumbnail.fields import ImageField

class Category(models.Model):

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    label = models.CharField('Libellé', max_length=64)

    def __unicode__(self):
        return self.label

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "label__icontains",)

class Size(models.Model):

    class Meta:
        verbose_name = "Taille"
        verbose_name_plural = "Tailles"

    label = models.CharField('Libellé', max_length=64)

    def __unicode__(self):
        return self.label

class Bike(models.Model):

    class Meta:
        verbose_name = "Vélo"
        verbose_name_plural = "Vélos"

    label = models.CharField('Nom du vélo', max_length=64)
    description = models.TextField('Description', max_length=1024)
    price = models.DecimalField('Tarif à la journée', max_digits=5, decimal_places=2)

    sizes = models.ManyToManyField(Size, verbose_name="Tailles disponibles")
    categories = models.ManyToManyField(Category, verbose_name="Catégories")

    picture = ImageField('Photo', upload_to='bikes/')

    def __unicode__(self):
        return self.label

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "label__icontains",)