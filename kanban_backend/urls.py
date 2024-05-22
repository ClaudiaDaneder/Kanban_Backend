from django.contrib import admin
from django.urls import path

from kanban_board import views
from kanban_board.views import BoardCreateView, BoardView, LoginView, RegisterView, TaskView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', BoardView.as_view()),
    path('boards/1/', TaskView.as_view()),
    path('boards/new/', BoardCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
]
