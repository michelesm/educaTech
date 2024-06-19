from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [

    path('', views.ProfessorListView.as_view(), name='professor_list'),
    path('professores/<pk>/', views.ProfessorDetailView.as_view(), name='professor_detail'),
    path('professores/<pk>/edit/', views.ProfessorCreateView.as_view(), name='professor_edit'),
    path('professor/<pk>/delete/', views.ProfessorDeleteView.as_view(), name='professor_delete'),
    path('professor/<pk>/edit/', views.ProfessorEditView.as_view(), name='professor_edit'),

]
