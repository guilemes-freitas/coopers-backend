from django.urls import path
from .views import DeleteCompletedView, DeleteIncompletedView, TaskView, UserCreateView, LoginView

urlpatterns = [
    path('accounts/', UserCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:task_id>/', TaskView.as_view()),
    path('tasks/completed/', DeleteCompletedView.as_view()),
    path('tasks/incompleted/', DeleteIncompletedView.as_view())
]