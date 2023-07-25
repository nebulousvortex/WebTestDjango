from django.urls import path
from . import views

urlpatterns = [
    #path('', views.GameHome.as_view(), name='game'),
    path('', views.lobby, name='riot_api'),
]