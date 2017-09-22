"""
Admin: App 'locacoes'
"""
from django.contrib import admin
from locacoes.models import Cliente, Locacao, Filme, Classificacao, Genero, StatusLocacao

admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Filme)
admin.site.register(Classificacao)
admin.site.register(Genero)
admin.site.register(StatusLocacao)
