from django.contrib import admin
from kanban_board.models import Board, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project_lead', 'deadline', 'created_at', 'created_by', 'board')
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at')

admin.site.register(Task, TaskAdmin)
admin.site.register(Board, BoardAdmin)
