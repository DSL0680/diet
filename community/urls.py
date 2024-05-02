from django.urls import path
from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('community/post/<int:id>/', views.view_post, name='view_post'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
]
