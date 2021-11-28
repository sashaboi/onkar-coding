from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework import serializers

from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls ={
        'List' : '/task-list',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    
    serializer = TaskSerializer(data = request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id =pk)
    serializer = TaskSerializer(instance = task,data = request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id =pk)
    task.delete()
    return Response("Item deleted")