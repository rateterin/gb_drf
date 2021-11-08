from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    link_to_repo = models.CharField(max_length=64)
