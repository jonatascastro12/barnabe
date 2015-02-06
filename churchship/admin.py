from django.contrib import admin
from churchship.models import Church, ChurchType, BarnabeUser, BarnabeUserChurch


class ChurchAdmin(admin.ModelAdmin):
    pass

class ChurchTypeAdmin(admin.ModelAdmin):
    pass

class BarnaberUserAdmin(admin.ModelAdmin):
    pass

class BarnaberUserChurchAdmin(admin.ModelAdmin):
    pass



# Register your models here.
admin.site.register(Church, ChurchAdmin)
admin.site.register(ChurchType, ChurchTypeAdmin)
admin.site.register(BarnabeUser, BarnaberUserAdmin)
admin.site.register(BarnabeUserChurch, BarnaberUserChurchAdmin)
