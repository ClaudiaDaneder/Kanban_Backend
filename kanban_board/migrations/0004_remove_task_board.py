# Generated by Django 5.0.6 on 2024-05-21 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0003_alter_task_deadline_board_task_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='board',
        ),
    ]
