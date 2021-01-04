from django.urls import path

from . import views

urlpatterns = [
    path('', views.triangle_form, name='triangle'),
    path('contact', views.contact_form, name="contact"),
]
