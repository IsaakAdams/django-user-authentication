from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_page/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout"),
]