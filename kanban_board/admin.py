from django.contrib import admin
from kanban_board.models import Board, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_lead', 'deadline')

admin.site.register(Task, TaskAdmin)
admin.site.register(Board)
