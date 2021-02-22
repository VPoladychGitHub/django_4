from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('aaa', views.choise, name='aaa'),
    path('bbb', views.CreateMyModelView.as_view(), name='bbb'),
    path('', views.new_person, name='person-create'),
    path('<int:pk>', views.person_edit, name='person-update'),
    # path('', views.PersonCreate.as_view(), name='person-create'),
    # path('<int:pk>', views.PersonUpdate.as_view(), name='person-update'),
]
