from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("player", views.player, name="player"),
    path("homepage", views.homepage, name="homepage"),
    path("home_page", views.home_page, name="home_page"),
]