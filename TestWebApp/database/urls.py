from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.UpdateHome.as_view(), name='data_base_home'),
    path('create_note', views.create_note, name='create_note'),
    path('note/<int:note_id>/', cache_page(60*5)(views.UpdateShow.as_view()), name='note'),
    path('not_login_user/', views.not_auth, name="not_auth"),
]
