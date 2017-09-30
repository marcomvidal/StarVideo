"""
URL Dispatcher: App 'locacoes'
"""
from django.conf.urls import url

from . import views


app_name = 'locacoes'

urlpatterns = [
    url(r'filmes/$',                        views.filmes_index,     name="filmes-index"),
    url(r'filmes/(?P<pk>[0-9]+)/$',         views.filmes_detalhes,  name="filmes-detalhes"),
    url(r'filmes/buscar/$',                 views.filmes_buscar,    name="filmes-buscar"),
    url(r'filmes/novo/$',                   views.filmes_criar,     name="filmes-criar"),
    url(r'filmes/(?P<pk>[0-9]+)/editar/$',  views.filmes_editar,    name="filmes-editar"),
    url(r'filmes/(?P<pk>[0-9]+)/excluir/$', views.filmes_excluir,   name="filmes-excluir"),
]
