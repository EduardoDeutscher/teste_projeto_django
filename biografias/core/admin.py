from django.contrib import admin
from . models import *

class pessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_modificacao']
    search_fields = ['nome']

# Register your models here.
admin.site.register(Pessoa, pessoaAdmin)