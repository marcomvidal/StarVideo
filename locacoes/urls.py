"""
URL Dispatcher: App 'locacoes'
"""
from django.conf.urls import url

from . import views


app_name = 'locacoes'

urlpatterns = [
    url(r'filmes/$',                        views.FilmeIndexView.as_view(), name="filmes-index"),
    url(r'filmes/novo/$',                   views.filmes_criar,             name="filmes-criar"),
    url(r'filmes/(?P<pk>[0-9]+)/editar/$',  views.filmes_editar,            name="filmes-editar"),
]
