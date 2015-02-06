# -*- charset utf8 -*-

from django.contrib import admin
from membership.models import Person, Member, MemberFunction
# Register your models here.

class MemberInline(admin.StackedInline):
	model = Member

class PersonAdmin(admin.ModelAdmin):
	inlines = [MemberInline]


admin.site.register(MemberFunction)
admin.site.register(Person, PersonAdmin)
