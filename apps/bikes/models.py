# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from sorl.thumbnail.fields import ImageField

class Category(models.Model):

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    label = models.CharField('Libellé', max_length=64)
    short_label = models.SlugField('Libellé raccourci', max_length=64)

    def __unicode__(self):
        return self.label

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "label__icontains",)

class Brand(models.Model):

    class Meta:
        verbose_name = "Marque"
        verbose_name_plural = "Marques"

    title = models.CharField('Nom', max_length=64)

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)


class Size(models.Model):

    class Meta:
        verbose_name = "Taille"
        verbose_name_plural = "Tailles"

    label = models.CharField('Libellé', max_length=64)

    def __unicode__(self):
        return self.label

class Bike(models.Model):

    BIKE_GENDER_LIST = (
        ('man', 'Homme'),
        ('woman', 'Femme'),
        ('child', 'Enfant')
        )

    class Meta:
        verbose_name = "Vélo"
        verbose_name_plural = "Vélos"

    label = models.CharField('Nom du modèle du vélo', max_length=64)
    description = models.TextField('Description', max_length=1024)
    price = models.DecimalField('Tarif à la journée', max_digits=8, decimal_places=2)

    second_hand = models.BooleanField('Vélo d’occasion', default=False)
    for_sale = models.BooleanField('À vendre', default=True, help_text='Décocher la case pour mettre le vélo dans l’offre location')

    brand = models.ForeignKey(Brand, verbose_name="Marque", null=True, blank=True)

    gender = models.CharField(max_length=20,choices=BIKE_GENDER_LIST, default='man')

    sizes = models.ManyToManyField(Size, verbose_name="Tailles disponibles")
    categories = models.ManyToManyField(Category, verbose_name="Catégories")

    visible = models.BooleanField(verbose_name="Visible", default=True)

    picture = ImageField('Photo', upload_to='bikes/')

    def __unicode__(self):
        return self.label

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "label__icontains",)