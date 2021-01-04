from django.urls import path

from . import views

urlpatterns = [
    #  path('', views.new_person, name='person-create'),
    path('', views.PersonCreate.as_view(), name='person-create'),
    path('<int:pk>', views.PersonUpdate.as_view(), name='person-update'),
]
