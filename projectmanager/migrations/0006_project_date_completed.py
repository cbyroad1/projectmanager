# Generated by Django 4.1.1 on 2022-09-28 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectmanager", "0005_project_completed"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="date_completed",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]