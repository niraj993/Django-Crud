from django.urls import path
from configs.routs import LOGIN_ROUTE,REGISTER_ROUTE,LOGOUT_ROUTE
from . import views

urlpatterns = [
    path(LOGIN_ROUTE,views.login,name="login"),
    path(REGISTER_ROUTE,views.register,name="register"),
    path(LOGOUT_ROUTE, views.logout_view, name='logout'),
]