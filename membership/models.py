# -*- coding: utf-8 -*-
import re
from django.db.models import permalink
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
from django.db import models
from barnabe.forms import CropImageModelField
from barnabe.utils import STATE_CHOICES
from churchship.models import Church


class MemberFunction(models.Model):
    
    def __str__(self):
        return self.name.encode('utf8')

    title = models.CharField(max_length=60, verbose_name='Título abrev.', help_text='Ex: Dc')
    name = models.CharField(max_length=255, verbose_name='Título', help_text='Ex: Diácono')
    title_female = models.CharField(max_length=60, verbose_name='Título abrev. Feminino', help_text = 'Ex: Dcª')
    name_female = models.CharField(max_length=255, verbose_name='Título Feminino', help_text = 'Ex: Diaconisa')

    class Meta:
        verbose_name = 'Função de membro'
        verbose_name_plural = 'Funções de membro'

class Person(models.Model):
    def __str__(self):
        return self.name.encode('utf8')

    timestamp = models.DateTimeField(default=timezone.now, auto_now_add=True)

    name = models.CharField(max_length=255, verbose_name='Nome', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'), flags=re.L)])

    photo = CropImageModelField(blank=True, upload_to='members/', verbose_name="Foto")

    cpf = models.CharField(max_length=14, verbose_name='CPF')
    rg = models.CharField(max_length=14, blank=True, null=True, verbose_name='RG')

    birth_date = models.DateField(verbose_name='Data de Nascimento')
    gender = models.CharField(max_length='1', verbose_name=_('Gender'), choices=[('M', _('Male')), ('F', _('Female'))])
    blood_type = models.CharField(max_length='2', blank=True, null=True, verbose_name=_('Blood Type'), choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-','B-'), ('O+', 'O+'), ('O-', 'O-')])

    email = models.EmailField(max_length='200')

    address_line = models.CharField(blank=True, max_length='300', verbose_name=_('Address'), validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, max_length='200', verbose_name=_('Neighborhood'), validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, max_length='200', verbose_name=_('City'), validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = models.CharField(blank=True, max_length='2', verbose_name='UF',choices=STATE_CHOICES)
    zipcode = models.CharField(blank=True, null=True, max_length='10')
    phone1 = models.CharField(blank=True, max_length='15', verbose_name='Telefone 1',)
    phone2 = models.CharField(blank=True, max_length='15', verbose_name='Telefone 2',)

    profession = models.CharField(blank=True, null=True, max_length='200', verbose_name=_('Profession'))
    work_place = models.CharField(blank=True, null=True, max_length='200', verbose_name=_('Work place'))

    father_name = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Father name'))
    mother_name = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Mother name'))
    marital_status = models.CharField(max_length='1', blank=True, null=True, choices=[('S', _('Single')), ('D', _('Divorced')), ('M', _('Married')), ('W', _('Widow')), ])
    spouse = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Spouse'))
    has_child = models.CharField(blank=True, null=True, max_length='1', verbose_name=_('Has Child?'), choices=[('Y', _('Yes')), ('N', _('No'))])
    how_many_child = models.PositiveSmallIntegerField(default=0)

    #TODO: Spouse - Foreign Key
    #TODO: Children - ManyToManyField or Foreing Key in a ChildrenObject

    class Meta:
        verbose_name = _('Person')

class Member(models.Model):

    SITUATION_CHOICES = [('A', _('Active')), ('I', _('Inactive'))]

    def __str__(self):
        return self.person.name.encode('utf8')

    previous_church = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Previous church'))
    previous_function = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Previous function'))
    baptism_date = models.DateField(verbose_name=_('Baptism date'))
    baptism_place = models.CharField(max_length='255',blank=True, null=True, verbose_name=_('Baptism place'))
    admission_date = models.DateField(blank=True, null=True, verbose_name=_('Admission date'))
    member_function = models.ForeignKey(MemberFunction, verbose_name="Função")
    situation = models.CharField(max_length=7, verbose_name="Situação", choices=SITUATION_CHOICES)
    church = models.ForeignKey(Church)
    person = models.OneToOneField(Person, null=True, verbose_name='Pessoa')

    def get_member_function(self):
        if self.person.gender == 'F':
            return self.member_function.name_female
        else:
            return self.member_function.name

    def get_member_function_display(self):
        return self.get_member_function()

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