from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.diary_list, name='diary_list'),
    path('create/', views.diary_create, name='diary_create'),
    path('<int:diary_id>/', views.diary_detail, name='diary_detail'),
    path('<int:diary_id>/update/', views.diary_update, name='diary_update'),
    path('<int:diary_id>/delete/', views.diary_delete, name='diary_delete'),
]
