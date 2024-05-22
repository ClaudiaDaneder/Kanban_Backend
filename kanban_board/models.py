from datetime import date
from django.conf import settings
from django.db import models

PRIORITY_CHOICES = ((1, 'High'),
                    (2, 'Medium'),
                    (3, 'Low'))

STATUS_CHOICES = ((1, 'To Do'),
                  (2, 'Do Today'),
                  (3, 'In Progress'),
                  (4, 'Done'))

class Board(models.Model):
    title = models.CharField(max_length=100)
    # owner = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    created_at = models.DateField(("Created"), default=date.today)

    def __str__(self):
        return self.title


class Task(models.Model):
    board = models.ForeignKey(
        Board,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    project_lead = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateField(("Created"), default=date.today)
    deadline = models.DateField(("Deadline"))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.title
