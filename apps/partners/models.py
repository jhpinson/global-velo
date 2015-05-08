# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from model_utils.models import TimeStampedModel
from ordered_model.models import OrderedModel
from sorl.thumbnail.fields import ImageField


class Partner(OrderedModel, TimeStampedModel):

    class Meta(OrderedModel.Meta):
        pass

    name = models.CharField('Nom', max_length=128)
    description = models.CharField('Description', max_length=512)

    website = models.URLField('Site internet', max_length=1024, null=True, blank=True)
    phone = models.CharField('numéro de téléphone', max_length=10, null=True, blank=True)
    email = models.EmailField('Adresse email', null=True, blank=True)

    active = models.BooleanField('Afficher ce partenaire sur le site', default=True)

    picture = ImageField('Logo', upload_to='partners/', null=True, blank=True)