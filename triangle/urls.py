from django.urls import path

from . import views

urlpatterns = [
    path('', views.triangle_form, name='triangle'),
    path('sendemail', views.send_email_form, name="send_email"),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contact_create', views.contact_create, name="contact_create"),
    path('contact', views.contact_form, name="contact"),
]
