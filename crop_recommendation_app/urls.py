from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("crop_prediction/", views.crop_prediction, name="crop_prediction"),
    path("fertilizer_prediction/", views.fertilizer_prediction, name="fertilizer_prediction"),
    path("crop_result/", views.crop_result, name="crop_result"),
    path("fertilizer_result/", views.fertilizer_result, name="fertilizer_result"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)