from django.urls import path
from . import views

urlpatterns = [
    path('trucking', views.trucking, name='trucking'),
]