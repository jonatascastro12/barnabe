# -*- coding: utf-8 -*-
import re
from django.contrib.auth.models import AbstractUser, User
from django.db.models import permalink
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
from django.db import models


class MemberFunction(models.Model):
    
    def __str__(self):
        return self.name.encode('utf8')

    title = models.CharField(max_length=60, verbose_name = 'Título abrev.', help_text = 'Ex: Dc')
    name = models.CharField(max_length=255, verbose_name = 'Título', help_text = 'Ex: Diácono')
    titleFemale = models.CharField(max_length=60, verbose_name = 'Título abrev. Feminino', help_text = 'Ex: Dcª')
    nameFemale = models.CharField(max_length=255, verbose_name = 'Título Feminino', help_text = 'Ex: Diaconisa')

    class Meta:
        verbose_name = 'Função de membro' 
        verbose_name_plural = 'Funções de membro'

class Person(models.Model):

    STATE_CHOICES = [
        ('','Selecione um estado'),('AC','Acre'),('AL','Alagoas'),('AM','Amazonas'),('AP','Amapá'),('BA','Bahia'),
        ('CE','Ceará'),('DF','Distrito Federal'),('ES','Espírito Santo'),('GO','Goiás'),('MA','Maranhão'),('MG','Minas Gerais'),
        ('MS','Mato Grosso do Sul'),('MT','Mato Grosso'),('PA','Pará'),('PB','Paraíba'),('PE','Pernambuco'),('PI','Piauí'),
        ('PR','Paraná'),('RJ','Rio de Janeiro'),('RN','Rio Grande do Norte'),('RO','Rondônia'),('RR','Roraima'),('RS','Rio Grande do Sul'),
        ('SC','Santa Catarina'),('SP','São Paulo'),('SE','Sergipe'),('TO','Tocantins'),
    ]

    def __str__(self):
        return self.name.encode('utf8')

    name = models.CharField(max_length=255, verbose_name = 'Nome', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'), flags=re.L)])
    cpf = models.CharField(max_length=14, verbose_name = 'CPF', validators=[RegexValidator('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', _(u'You should type de 11 digits of your CPF.'))])
    birthDt = models.DateField(verbose_name = 'Data de Nascimento')
    gender = models.CharField(max_length='1', verbose_name = 'Sexo', choices = [('M','Masculino'), ('F','Feminino')])
    email = models.EmailField(max_length='200')
    address_line = models.CharField(blank=True, max_length='300', verbose_name = 'Endereço', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, max_length='200', verbose_name = 'Bairro', validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, max_length='200', verbose_name = 'Cidade', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = models.CharField(blank=True, max_length='2', verbose_name = 'UF',choices=STATE_CHOICES)
    phone1 = models.CharField(blank=True, max_length='15', verbose_name = 'Telefone 1',)
    phone2 = models.CharField(blank=True, max_length='15', verbose_name = 'Telefone 2',)
    photo = models.ImageField(blank=True, upload_to='members/', verbose_name="Foto")
    photo_original = models.CharField(null=True, max_length=255)
    photo_crop_data = models.CharField(null=True, max_length=255)

    class Meta:
        verbose_name = 'Pessoa'


class ChurchType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Church Type')


class BarnabeUser(models.Model):
    user = models.OneToOneField(User)

class Church(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', blank=True)
    phone1 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 1')
    phone2 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 2')
    type = models.ForeignKey(ChurchType)
    church_mother = models.ForeignKey('self', null=True, blank=True)
    barnabe_user = models.ForeignKey(BarnabeUser)

    def __str__(self):
        return self.name.encode('utf8')

    class Meta:
        verbose_name = _('Church')

class Member(models.Model):

    SITUATION_CHOICES = [('A','Ativo'), ('I','Inativo')]

    def __str__(self):
        return self.person.name.encode('utf8')

    baptismDt = models.DateField(verbose_name='Data de Batismo')
    memberFunction = models.ForeignKey(MemberFunction, verbose_name="Função")
    situation = models.CharField(max_length=7, verbose_name="Situação", choices=SITUATION_CHOICES)
    church = models.ForeignKey(Church)
    person = models.OneToOneField(Person, null=True, verbose_name='Pessoa')

    @permalink
    def get_absolute_url(self):
        return ('member_detail', (), {'pk': self.id})

    class Meta:
        verbose_name = _('Member')



'''
# Create your models here.
class Address(models.Model):

    ADDRESS_CHOICES = [
        ('RES', 'Residencial'),
        ('COM', 'Comercial')
    ]

    def __str__(self):
        return self.address_line

    address_type = models.CharField(max_length=100, verbose_name = 'Tipo', default = 'Casa', choices = ADDRESS_CHOICES)
    address_line = models.CharField(max_length=255, verbose_name = 'Endereço')
    city = models.CharField(max_length=255, verbose_name = 'Cidade')
    state = models.CharField(max_length=50, verbose_name = 'UF')
    country = models.CharField(max_length=50, verbose_name = 'País')
    person = models.ForeignKey(Person, verbose_name = "Pessoa")


    class Meta:
        verbose_name = 'Endereço'   

class Phone(models.Model):

    PHONE_CHOICES = [
        ('FRE', 'Fixo Residencial'),
        ('FCO', 'Fixo Comercial'),
        ('FAX', 'Fax'),
        ('CLR', 'CLARO'),
        ('TIM', 'TIM'),
        ('OI', 'OI'),
        ('VIV', 'VIVO'),
        ('NEX', 'NEXTEL')
    ]

    phone_type = models.CharField(max_length=100, verbose_name = 'Tipo', choices = PHONE_CHOICES)
    phone_number = models.CharField(max_length=15, verbose_name = 'Nº Telefone')
    ramal = models.CharField(max_length=15, null = True, verbose_name = 'Ramal')
    person = models.ForeignKey(Person, verbose_name = "Pessoa")

    class Meta:
        verbose_name = 'Telefone'

'''