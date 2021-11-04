from django.urls import path
from .views import TaskView, UserCreateView, LoginView

urlpatterns = [
    path('accounts/', UserCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:task_id>/', TaskView.as_view())
]