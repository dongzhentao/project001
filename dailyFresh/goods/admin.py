from django.contrib import admin
from models import *


class Typeadmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gkucun', 'isDelete']
    list_per_page = 20


admin.site.register(TypeInfo, Typeadmin)
admin.site.register(GoodsInfo, GoodsAdmin)
