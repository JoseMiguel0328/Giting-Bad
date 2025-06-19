from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing_page, name="landing"),
    path('services', views.services, name="services"),
]