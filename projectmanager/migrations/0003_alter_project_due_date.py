# Generated by Django 4.1.1 on 2022-09-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectmanager", "0002_alter_project_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="due_date",
            field=models.DateTimeField(blank=True),
        ),
    ]
