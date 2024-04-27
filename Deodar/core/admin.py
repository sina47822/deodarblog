from django.contrib import admin
from .models import MainMenu , SubMenu


class SubMenuInline(admin.TabularInline) :
    model = SubMenu

class MainMenuAdmin(admin.ModelAdmin) :
    inlines = [SubMenuInline]

admin.site.register(MainMenu , MainMenuAdmin)
admin.site.register(SubMenu)