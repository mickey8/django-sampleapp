from django.contrib import admin

from .models import Prefecture, Shop


class PrefectureAdmin(admin.ModelAdmin):
    pass


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'kana_name',)

admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Shop, ShopAdmin)
