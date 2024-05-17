from django.shortcuts import render

# Create your views here    

def goal_page(request):
    return render(request,'ry/goal.html')


def signup_page(request):
    return render(request,'ry/signup.html')