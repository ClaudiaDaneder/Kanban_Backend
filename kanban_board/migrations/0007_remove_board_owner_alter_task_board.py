# Generated by Django 5.0.6 on 2024-05-22 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0006_alter_task_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='owner',
        ),
        migrations.AlterField(
            model_name='task',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kanban_board.board'),
        ),
    ]
