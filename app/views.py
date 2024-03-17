from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.response import Response



class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            return Response({'token': 'valid'})
        except:
            return Response({'token': 'invalid'})


@api_view(['GET'])
def apiOverView(request):
    return Response("OKY")

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def taskDelete(request,pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response("Data deleted")


@api_view(['GET'])
@permission_classes([AllowAny])
def myview(requets):
    return Response("You Are Ready")



