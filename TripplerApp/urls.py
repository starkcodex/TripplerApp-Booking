
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('' , include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('hotel/' , include('apps.hotels.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
