from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logistics', views.logistics, name='logistics'),
    path('about', views.about, name='about'),
]