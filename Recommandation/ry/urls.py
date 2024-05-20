


from django.urls import path
from . import views
from .views import goal_list

urlpatterns = [
    path('goal/', goal_list, name='goal-list'),
    path('', views.signup_page),
]