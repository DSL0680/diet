from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food_search'
urlpatterns = [
    path('search/', views.search_food, name='search'),
    path('save/', views.save_food, name='save'),
    path('food_list/', views.food_list, name='food_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
