# Generated by Django 5.0.6 on 2024-05-24 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0013_rename_board_id_task_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 5, 24), verbose_name='Created'),
        ),
    ]