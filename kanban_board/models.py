from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

PRIORITY_CHOICES = ((1, 'Low'),
                    (2, 'Medium'),
                    (3, 'Urgent'))

STATUS_CHOICES = ((1, 'To Do'),
                  (2, 'Do Today'),
                  (3, 'In Progress'),
                  (4, 'Done'))

class Board(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(("Created"), auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    board = models.ForeignKey(
        Board,
        related_name='board',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    project_lead = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="project_lead"
    )
    created_at = models.DateField(("Created"), auto_now=True)
    deadline = models.DateField(("Deadline"))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_by"
        )


    def __str__(self):
        return self.title
