from django.urls import path
from . import views
urlpatterns=[
    path("",views.index ,name="index"),
    path("register/",views.register ,name="register"),
    path("login/",views.login ,name="login"),
    path("loginbase/",views.loginbase ,name="loginbase"),
    path("writeblog/",views.writeblog ,name="writeblog"),
    path("list/",views.list ,name="list"),
    path("details/",views.details ,name="details"),
]
