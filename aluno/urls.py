from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='aluno_list'),
    path('create/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('aluno/<pk>/detail-ajax/', views.aluno_detail_ajax, name='aluno_detail_ajax'),
    path('<pk>/update/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    path('<pk>/delete/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
]
