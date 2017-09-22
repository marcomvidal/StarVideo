"""
URL Dispatcher: App 'locacoes'
"""
from django.conf.urls import url

from . import views


app_name = 'locacoes'
urlpatterns = [
    url(r'filmes/$', views.FilmeIndexView.as_view(), name="filme-index"),
    url(r'filmes/novo/$', views.filmes_create, name="filme-create"),
    url(r'filmes/(?P<pk>[0-9]+)/editar/$', views.filmes_edit, name="filme-editar"),
    url(r'filmes/sucesso/$', views.success, name="success"),
    url(r'filmes/falha/$', views.fail, name="fail"),
]
