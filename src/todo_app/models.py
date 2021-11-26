from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    link_to_repo = models.CharField(max_length=64, blank=True, null=True)
    users = models.ManyToManyField('users.User', related_name='project_users')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект "{self.name}"'


class Todo(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='todo_project')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    user_created = models.OneToOneField('users.User',
                                        on_delete=models.CASCADE,
                                        editable=False)

    class Meta:
        verbose_name = 'ToDo заметка'
        verbose_name_plural = 'ToDo заметки'

    def __str__(self):
        return f'ToDo заметка для проекта "{Todo.project.name}"'
