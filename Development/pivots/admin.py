from django.contrib import admin

from .models import staff,group
# Register your models here.

class staffAdmin(admin.ModelAdmin):
    list_display = ("name","uni_id")

class groupAdmin(admin.ModelAdmin):
    list_display = ("name","code")
    

admin.site.register(staff,staffAdmin)
admin.site.register(group,groupAdmin)