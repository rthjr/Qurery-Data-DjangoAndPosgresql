from django.shortcuts import render
from .models import Goal



def signup_page(request):
    return render(request,'ry/signup.html')


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'ry/goal.html', {'goals': goals})

