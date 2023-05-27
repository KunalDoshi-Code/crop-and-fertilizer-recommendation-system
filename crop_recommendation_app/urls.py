from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("crop_prediction/", views.crop_prediction, name="crop_prediction"),
    path("fertilizer_prediction/", views.fertilizer_prediction, name="fertilizer_prediction"),
    path("crop_result/", views.crop_result, name="crop_result"),
    path("fertilizer_result/", views.fertilizer_result, name="fertilizer_result"),
]
