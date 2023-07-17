from django.urls import path, re_path
from . import views
from django.views.decorators.cache import cache_page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='info'),
    re_path(r'^archive/(?P<year>[0-9]{4})', views.archive),
    path('logout/', views.logout_user, name="logout"),
    path('login/', cache_page(60*5)(views.LoginUser.as_view()), name="login"),
    path('register/', views.RegisterUser.as_view(), name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

