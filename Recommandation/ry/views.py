from django.shortcuts import render

from .models import Goal


# rest api 
# from . import serializers
# from . import models
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# Create your views here    

# def goal_page(request):
#     return render(request,'ry/goal.html')


def signup_page(request):
    return render(request,'ry/signup.html')


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'ry/goal.html', {'goals': goals})


# rest api
# class goal_view(APIView):
#     def get(self, request, id=None):
#         if id:
#             item = models.goal.objects.get(id=id)
#             serializer = serializers.goalserializer(item)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#         items = models.goal.objects.all()
#         serializer = serializers.goalserializer(items, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = serializers.goalserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, id=None):
#         item = models.goal.objects.get(id=id)
#         serializer = serializers.goalserializer(item, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None):
#         item = models.goal.objects.filter(id=id)
#         print(item)
#         item.delete()
#         return Response({"status": "success", "data": "Item Deleted"})