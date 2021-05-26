from django.urls import path
from . import views

app_name = 'usertrack'

urlpatterns = [
    path('', views.Tracking, name='tracking'),
]