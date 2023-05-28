from django.urls import path
from . import views

app_name="nn"
urlpatterns = [
    path("", views.home, name="home"),
    path("theory", views.theory, name="theory"),
    path("user-guide", views.user_guide, name="user_guide"),
    path("app/step1", views.upload_csv, name="step1_upload_csv"),
    path("app/step2", views.choose_data_format, name="step2_choose_data_format"),
    path("app/step3", views.script, name="step3_hidden_layers")
]