from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)