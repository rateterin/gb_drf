# Generated by Django 3.2.8 on 2021-11-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='project',
            field=models.ManyToManyField(related_name='project_users', to='todo_app.Project'),
        ),
    ]
