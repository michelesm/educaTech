from django.urls import path
from. import views

urlpatterns = [

    path('', views.cursos_list, name='curso_list'),
    path('curso/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detail'),
    path('create/', views.CursoCreateView.as_view(), name='curso_create'),
    path('cursos/<pk>/update/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('cursos/<pk>/delete/', views.CursoDetailView.as_view(), name='curso_delete'),
    path('turmas/', views.TurmaListView.as_view(), name='turma_list'),
    path('turmas/<pk>/', views.TurmaDetailView.as_view(), name='turma_detail'),
]