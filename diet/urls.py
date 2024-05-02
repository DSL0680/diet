from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('diary/', include('diary.urls')),
    path('search/', include('search.urls')),
    path('food/', include('food_search.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
