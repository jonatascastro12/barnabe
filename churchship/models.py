# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext as _
from barnabe.utils import STATE_CHOICES, BARNABE_PERMISSION_CHOICES

class ChurchType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Church Type')

# Create your models here.
class Church(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', blank=True)
    email = models.EmailField(blank=True, null=True, max_length='200')
    address_line = models.CharField(blank=True, null=True, max_length='300', verbose_name = 'Endereço', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Bairro', validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Cidade', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = models.CharField(blank=True, null=True,  max_length='2', verbose_name = 'UF',choices=STATE_CHOICES)
    phone1 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 1')
    phone2 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 2')
    type = models.ForeignKey(ChurchType)
    is_mother = models.BooleanField(default=True)
    church_mother = models.ForeignKey('self', null=True, blank=True)
    logo = models.ImageField(blank=True, upload_to='church/', verbose_name="Logo")
    logo_original = models.CharField(null=True, max_length=255, blank=True)
    logo_crop_data = models.CharField(null=True, max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('church_detail', (), {'pk': self.id})

    class Meta:
        verbose_name = _('Church')