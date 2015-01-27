# -*- charset utf8 -*-

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from membership.models import Person, Member, MemberFunction, Church, ChurchType, BarnabeUser
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.

class MemberInline(admin.StackedInline):
	model = Member

class PersonAdmin(admin.ModelAdmin):
	inlines = [MemberInline]

class ChurchAdmin(admin.ModelAdmin):
    pass

class ChurchTypeAdmin(admin.ModelAdmin):
    pass

class BarnaberUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(MemberFunction)
admin.site.register(Person, PersonAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(ChurchType, ChurchTypeAdmin)
admin.site.register(BarnabeUser, BarnaberUserAdmin)
