from django.urls import path

from . import views

urlpatterns = [
    path('', views.async_fun, name='async_fun'),
]