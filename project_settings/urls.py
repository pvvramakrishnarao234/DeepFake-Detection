"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include,re_path

from django.conf import settings
# from django.conf.urls import  url?
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/',admin.site.urls),
    re_path('', include('ml_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
