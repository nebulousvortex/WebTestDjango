from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatHome.as_view(), name='chat')
]