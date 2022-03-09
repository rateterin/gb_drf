from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelCreateSerializer(ModelSerializer):
    user_created = serializers.HiddenField(default=None)

    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        user_created = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user_created = request.user
        validated_data.update(user_created=user_created)
        self.is_valid()
        return Todo.objects.create(**validated_data)


class TodoModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
