# Generated by Django 5.0.6 on 2024-05-24 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0016_alter_board_created_at_alter_task_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
    ]
