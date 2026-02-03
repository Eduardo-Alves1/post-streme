from django.contrib import admin
from .models import PubliModel


@admin.register(PubliModel)
class PubliAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criado_em")
    search_fields = ("titulo", "conteudo")
