# Generated by Django 4.1.1 on 2022-09-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectmanager", "0010_alter_task_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="has_tasks",
            field=models.BooleanField(default=False),
        ),
    ]
