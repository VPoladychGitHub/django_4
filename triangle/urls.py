from django.urls import path

from . import views

urlpatterns = [
    path('', views.triangle_form, name='triangle'),
    path('sendemail', views.send_email_form, name="send_email"),
    path('contact', views.contact_form, name="contact"),
]
