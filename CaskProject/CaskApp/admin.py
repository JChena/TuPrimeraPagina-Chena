from django.contrib import admin

from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Producto)
admin.site.register(models.Cata)
admin.site.register(models.Compra)
