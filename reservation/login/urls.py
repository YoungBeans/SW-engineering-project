
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path("find/password/", views.find_pwd, name="find_pwd"),
    path('find/password/change/', views.change_pwd, name="change_pwd"),
    path('user/review/', views.show_review, name="show_review"),
    path('user/review/write/', views.write_review, name="write_review"),
    path('user/review/myreview/<int:pk>/', views.my_review, name="my_review"),
    path('user/review/myreview/modify/<int:pk>/', views.modify_review, name="modify_review"),
    path("review/search/", views.search_review, name="search_review"),
    path("review/delete/<int:pk>/", views.review_delete, name="review_delete"),
]
