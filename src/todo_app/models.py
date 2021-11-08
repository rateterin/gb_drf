from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    link_to_repo = models.CharField(max_length=64)
    users = models.ManyToManyField('users.User', related_name='project_users')


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_created = models.OneToOneField('users.User', on_delete=models.CASCADE)
