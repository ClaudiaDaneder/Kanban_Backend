# Generated by Django 5.0.6 on 2024-05-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0015_alter_board_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Created'),
        ),
    ]