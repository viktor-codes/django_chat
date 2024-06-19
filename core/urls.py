from django.urls import path

from . import views

urlpatterns = [
    path("", views.front_page, name="frontpage"),
    path("signup/", views.signup, name="signup")
]
