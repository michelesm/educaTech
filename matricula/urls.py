from django.urls import path
from . import views

app_name = 'matricula'



urlpatterns = [
    path('matriculas/', views.matricula_list, name='matricula_list'),
    path('matriculas/create/', views.matricula_create, name='matricula_create'),
    path('matriculas/<pk>/edit/', views.matricula_edit, name='matricula_edit'),
    path('matriculas/<pk>/delete/', views.matricula_delete, name='matricula_delete'),
    path('matriculas/<pk>/', views.matricula_detail, name='matricula_detail'),
    path('matriculas/get_turmas/', views.get_turmas, name='get_turmas'),

]