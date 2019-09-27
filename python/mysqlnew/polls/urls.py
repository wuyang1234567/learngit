from django.urls import path
from . import views

urlpatterns = [
    path("",views.show_class,name="show_class"),
    path("login/",views.login,name="login"),
]