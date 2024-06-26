from django.urls import path
from. import views


app_name = 'documentos'

urlpatterns = [
    path('documentos/', views.documento_list, name='documento_list'),
    path('documentos/create/', views.documento_create, name='documento_create'),
    path('documentos/<pk>/edit/', views.documento_edit, name='documento_edit'),
    path('documentos/<pk>/delete/', views.documento_delete, name='documento_delete'),
]