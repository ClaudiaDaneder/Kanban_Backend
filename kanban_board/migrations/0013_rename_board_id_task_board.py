# Generated by Django 5.0.6 on 2024-05-23 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0012_rename_board_task_board_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='board_id',
            new_name='board',
        ),
    ]