from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),

    path(
        'funcionarios/',
        views.FuncionarioListView.as_view(),
        name='lista_funcionarios'
    ),

    path(
        'funcionario/cadastrar/',
        views.FuncionarioCreateView.as_view(),
        name='cadastra_funcionario'
    ),

    path(
        'funcionario/excluir/<int:pk>',
        views.FuncionarioDeleteView.as_view(),
        name='deleta_funcionario'
    ),

    path(
        'funcionario/<id>',
        views.FuncionarioUpdateView.as_view(),
        name='atualiza_funcionario'
    ),
]