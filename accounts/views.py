from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Tasks
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from accounts.serializers import TaskSerializer, UserSerializer

class UserCreateView(APIView):
  def post(self, request):
    try:

      user = User.objects.create_user(
        username=request.data['username'], 
        password=request.data['password']
      )

      serializer = UserSerializer(user, many=False)

      return Response(serializer.data, status=status.HTTP_201_CREATED) 
    except IntegrityError:
      return Response({"errors":"User already exists"}, status=status.HTTP_409_CONFLICT)

    
class LoginView(APIView):
  def post(self, request):
    user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
          )
          
    if user:
        token = Token.objects.get_or_create(user=user)[0]
        return Response({"token":str(token)}, status=status.HTTP_200_OK)
    return Response({"errors":"User not registered"}, status=status.HTTP_401_UNAUTHORIZED)
    

class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        task = Tasks.objects.create(
            title=request.data['title'],
            completed=False,
            user_id=request.user
        )

        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, task_id=''):
        try:
            serializer = TaskSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            task = Tasks.objects.get(id=task_id)
            task.title = request.data["title"]
            task.completed = request.data["completed"]
            task.save()
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"errors": "missing fields"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, task_id=''):
        try:
            if task_id:
                Tasks.objects.get(id=task_id).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            Tasks.objects.filter(user_id=request.user.id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"errors": "no task found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, task_id=''):
        if task_id:
            try:
                task = Tasks.objects.get(id=task_id)
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"errors": "invalid task_id"}, status=status.HTTP_404_NOT_FOUND)
        
        tasks = Tasks.objects.filter(user_id=request.user.id)
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)