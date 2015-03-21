# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

class Size(models.Model):

    labal = models.CharField('Libellé', max_length=64)

class Bike(models.Model):

    name = models.CharField('Nom du vélo', max_length=64)