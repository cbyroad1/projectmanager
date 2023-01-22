from django.db import models
from django.contrib.auth.models import User 
import datetime


# Create your models here.

class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project_title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(blank=True, null=True)
    has_tasks = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title
    
    def set_complete(self):
        self.completed = True
        self.date_completed = datetime.datetime.now()
        self.save()
    
    def add_tasks(self):
        self.has_tasks=True
        self.save()


class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, db_column="project_title", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def set_complete(self):
        self.completed = True
        self.date_completed = datetime.datetime.now()
        self.save()

    
