from django.contrib import admin
from . import models


admin.site.register(models.ResourceType)
admin.site.register(models.Resource)
