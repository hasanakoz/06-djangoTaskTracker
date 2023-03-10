from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Tasktracker
from .serializers import TaskSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def task_list_create(request):
    if request.method == 'GET':
        tasks = Tasktracker.objects.filter(is_done=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def task_detail(request, id):
    task = get_object_or_404(Tasktracker, id=id)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response({'message': 'task deleted successfully'})


class Tasks(ListCreateAPIView):
    queryset = Tasktracker.objects.filter(is_done=False)
    serializer_class = TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tasktracker.objects.filter(is_done=False)
    serializer_class = TaskSerializer
