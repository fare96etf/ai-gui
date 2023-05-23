from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("theory", views.theory, name="nn_theory"),
    path("user-guide", views.user_guide, name="user_guide"),
    path("app", views.script, name="nn_training")
]