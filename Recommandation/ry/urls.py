


from django.urls import path
from . import views

# rest framwork
# urlpatterns = [
#     path('goal/', goal_view.as_view()),
#     path('goal/<int:id>', goal_view.as_view()),
#     path('', views.signup_page),
# ]


from .views import goal_list

urlpatterns = [
    path('goal/', goal_list, name='goal-list'),
    path('', views.signup_page),
]