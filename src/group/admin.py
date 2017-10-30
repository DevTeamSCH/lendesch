from django.contrib import admin
from . import models


@admin.register(models.LenderGroup)
class LenderGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('administrators', )
