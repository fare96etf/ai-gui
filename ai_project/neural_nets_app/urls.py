from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("theory", views.theory, name="nn_theory"),
    path("nn", views.script, name="nn_training")
]