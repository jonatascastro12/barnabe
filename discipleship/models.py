# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from membership.models import Member
# Create your models here.

class Discipler(models.Model):
	member = models.ForeignKey(Member)
    
	class Meta:
		verbose_name = 'Discipulador'
		verbose_name_plural = 'Discipuladores'

class Disciple(models.Model):
	member = models.ForeignKey(Member, verbose_name = 'Membro')
	discipler = models.ForeignKey(Discipler, verbose_name = 'Discipulador')

	class Meta:
		verbose_name = 'Discipulo'


class Meeting(models.Model):
	monitors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name = 'Monitor')
	discipler = models.ForeignKey(Discipler, verbose_name = 'Discipulador')
	disciple = models.ForeignKey(Disciple, verbose_name = 'Discipulo')
	datetime = models.DateTimeField(verbose_name = 'Horário')
	description = models.TextField(verbose_name = 'Descrição')

	class Meta:
		verbose_name = 'Reunião'
		verbose_name_plural = 'Reuniões'