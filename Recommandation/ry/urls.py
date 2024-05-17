
from django.urls import path
from . import views


urlpatterns = [
    path('goal/', views.goal_page),
    path('', views.signup_page),
]