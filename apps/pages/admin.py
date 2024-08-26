from django.contrib import admin

# Register your models here.
from pages import models

admin.site.register(models.Pagina)
admin.site.register(models.TipoBloco)
admin.site.register(models.Conteudo)
admin.site.register(models.Blocos)