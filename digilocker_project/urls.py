# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from .settings import MEDIA_URL,MEDIA_ROOT

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('locker.urls')),
# ] + static(MEDIA_URL, document_root=MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('locker.urls')),
]

# ✅ Serve media files correctly (ONLY if using local storage)
if settings.DEBUG and hasattr(settings, 'MEDIA_URL'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
