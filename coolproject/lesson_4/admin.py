from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Example)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Product)
admin.site.register(models.Categories)
admin.site.register(models.Place)
admin.site.register(models.Hotel)
admin.site.register(models.Manager)