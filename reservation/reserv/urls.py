
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserv_home, name="resrv_home"),
    path("check/", views.reserv_check, name="reserv_check"),
    path("modify/<int:pk>/", views.reserv_modify_render, name="reserv_modify"),
    path("modify/<int:pk>/success/", views.reserv_modify, name="reserv_modify_success"),
    path("none/user/", views.non_user_reservate, name="non_user_reservation"),
    path("none/user/check/", views.non_user_reservate_check, name="non_user_reservate_check"),
    path("none/user/delete/", views.non_user_delete, name="non_user_delete"),
]
