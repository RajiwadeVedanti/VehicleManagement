from django.urls import path
from vehicleapp.views import *

urlpatterns = [
    path('', user.home, name="home"),
    path('login',user.login_user,name="login_user"),
    path('user', user.get_user, name="get_user"),
    path('user/add', user.add_user, name="add_user"),
    path('user/create', user.create_user, name="create_user")

]