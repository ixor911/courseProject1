from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class Admin(UserAdmin):
    pass


admin.site.register(models.User)
admin.site.register(models.Gender)
admin.site.register(models.Message)
admin.site.register(models.WordGroup)
admin.site.register(models.Word)
admin.site.register(models.Result)


