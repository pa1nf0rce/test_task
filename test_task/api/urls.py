from api import views
from django.urls import path

urlpatterns = [
    path('cars/', views.car_list),
    path('cars/<uuid:uuid>/', views.car_detail),
    path('generate/', views.car_generate),
    path('generate/<int:amount>/', views.car_generate),
]
