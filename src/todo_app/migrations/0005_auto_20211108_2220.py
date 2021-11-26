# Generated by Django 3.2.8 on 2021-11-08 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0004_alter_todo_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link_to_repo',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user_created',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
