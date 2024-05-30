from django.contrib import admin
from django.urls import path

from kanban_board import views
from kanban_board.views import BoardCreateView, BoardDetailView, BoardListView, LoginView, LogoutView, ProfileView, RegisterView, TaskCreateView, TaskDetailView, TaskListView, UserListView, UserTaskListView
# , BoardDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlist/', UserListView.as_view()),
    path('boards/', BoardListView.as_view()),
    path('boards/<int:board_id>/tasks/', TaskListView.as_view()),
    path('boards/<int:pk>/details/', BoardDetailView.as_view()),
    path('boards/new/', BoardCreateView.as_view()),
    path('tasks/new/', TaskCreateView.as_view()),
    path('tasks/<int:pk>/details/', TaskDetailView.as_view()),
    path('tasks/', UserTaskListView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterView.as_view())
]
