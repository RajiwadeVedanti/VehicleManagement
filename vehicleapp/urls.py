from django.urls import path
from vehicleapp.views import *

urlpatterns = [
    path('home', user.home, name="home"),
    path('login', user.login_user,name="login_user"),
    path('logout', user.logout_user, name="logout_user"),
    path('user', user.get_user, name="get_user"),
    path('user/add', user.add_user, name="add_user"),
    path('user/create', user.create_user, name="create_user"),
    path('user/view/<int:pk>', user.view_user, name="view_user"),
    path('user/edit/<int:pk>', user.edit_user, name="edit_user"),
    path('user/delete/<int:pk>', user.delete_user, name="delete_user"),

    # Vehicle URLs
    path('vehicle',vehicle.get_vehicle, name="get_vehicle"),
    path('vehicle/add', vehicle.add_vehicle, name="add_vehicle"),
    path('vehicle/create', vehicle.create_vehicle, name="create_vehicle"),
    path('vehicle/view/<int:pk>', vehicle.view_vehicle, name="view_vehicle"),
    path('vehicle/edit/<int:pk>', vehicle.edit_vehicle, name="edit_vehicle"),
    path('vehicle/delete/<int:pk>', vehicle.delete_vehicle, name="delete_vehicle")

]