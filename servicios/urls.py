from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.list_carro, name ='list_carro'),
    url(r'^servicios/nuevo/$', views.servicio_nuevo, name='servicio_nuevo'),
    url(r'^servicios/(?P<pk>[0-9]+)/$', views.carro_detail, name='carro_detail'),
    url(r'^servicios/(?P<pk>[0-9]+)/edit/$', views.carro_edit, name='carro_edit'),
    url(r'^servicios/(?P<pk>\d+)/remove/$', views.carro_remove, name='carro_remove'),

    url(r'^clientes/list/$', views.list_cliente, name ='list_cliente'),
    url(r'^clientes/nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
    url(r'^clientes/(?P<pk>[0-9]+)/$', views.cliente_detail, name='cliente_detail'),
    url(r'^clientes/(?P<pk>[0-9]+)/edit/$', views.cliente_editar, name='cliente_editar'),
    url(r'^clientes/(?P<pk>\d+)/remove/$', views.cliente_remove, name='cliente_remove'),

    url(r'^tipos/list/$', views.list_tipo, name ='list_tipo'),
    url(r'^tipos/nuevo/$', views.tipo_nuevo, name='tipo_nuevo'),
    url(r'^tipos/(?P<pk>[0-9]+)/$', views.tipo_detail, name='tipo_detail'),
    url(r'^tipos/(?P<pk>[0-9]+)/edit/$', views.tipo_editar, name='tipo_editar'),
    url(r'^tipos/(?P<pk>\d+)/remove/$', views.tipo_remove, name='tipo_remove'),
    ]
