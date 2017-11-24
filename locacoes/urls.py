"""
URL Dispatcher: App 'locacoes'
"""
from django.conf.urls import url

from . import views


app_name = 'locacoes'

urlpatterns = [
    url(r'filmes/$',                            views.FilmeListView.as_view(),          name="filmes-index"),
    url(r'filmes/(?P<pk>[0-9]+)/$',             views.FilmeDetailView.as_view(),        name="filmes-detalhes"),
    url(r'filmes/buscar/$',                     views.filmes_buscar,                    name="filmes-buscar"),
    url(r'filmes/novo/$',                       views.filmes_criar,                     name="filmes-criar"),
    url(r'filmes/(?P<pk>[0-9]+)/editar/$',      views.filmes_editar,                    name="filmes-editar"),
    url(r'filmes/(?P<pk>[0-9]+)/excluir/$',     views.FilmeDeleteView.as_view(),        name="filmes-excluir"),
    url(r'clientes/$',                          views.ClienteListView.as_view(),        name="clientes-index"),
    url(r'clientes/(?P<pk>[0-9]+)/$',           views.ClienteDetailView.as_view(),      name="clientes-detalhes"),
    url(r'clientes/buscar/$',                   views.clientes_buscar,                  name="clientes-buscar"),
    url(r'clientes/novo/$',                     views.clientes_criar,                   name="clientes-criar"),
    url(r'clientes/(?P<pk>[0-9]+)/editar/$',    views.clientes_editar,                  name="clientes-editar"),
    url(r'clientes/(?P<pk>[0-9]+)/excluir/$',   views.ClienteDeleteView.as_view(),      name="clientes-excluir"),
    url(r'locacoes/novo/$',                     views.locacoes_criar,                   name="locacoes-criar"),
    url(r'locacoes/(?P<pk>[0-9]+)/editar/$',    views.locacoes_editar,                  name="locacoes-editar"),
    url(r'locacoes/(?P<pk>[0-9]+)/cliente/$',   views.locacoes_addcliente,              name="locacoes-addcliente"),
    url(r'locacoes/(?P<pk>[0-9]+)/filme/$',     views.locacoes_addfilme,                name="locacoes-addfilme"),
]
