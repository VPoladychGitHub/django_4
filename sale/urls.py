from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.CityListView.as_view(), name='cities'),
    path('city/<int:pk>', views.CityDetailView.as_view(), name='city-detail'),
    path('city/create/', views.CityCreate.as_view(), name='city-create'),
    path('city/<int:pk>/update/', views.CityUpdate.as_view(), name='city-update'),
    path('city/', views.CityDelete.as_view(), name='authors'),
    path('city/<int:pk>/delete/', views.CityDelete.as_view(), name='city-delete'),
    path('provider/create/', views.ProviderCreate.as_view(), name='provider-create'),
]
