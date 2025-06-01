from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),

    path('vendas/', views.venda_list, name='venda_list'),
    path('vendas/novo/', views.venda_create, name='venda_create'),
    path('vendas/<int:pk>/editar/', views.venda_update, name='venda_update'),
    path('vendas/<int:pk>/excluir/', views.venda_delete, name='venda_delete'),
]
