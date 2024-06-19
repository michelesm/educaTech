from django.urls import path
from . import views
from .views import AlunoEditView

app_name = 'aluno'

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='aluno_list'),
    path('create/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('<pk>/delete/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
    path('aluno/<pk>/edit/', views.AlunoEditView.as_view(), name='aluno_edit'),
]
