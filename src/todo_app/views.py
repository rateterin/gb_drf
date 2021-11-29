from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .filters import ProjectFilter

from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class TodoPagination(PageNumberPagination):
    page_size = 20


class ProjectModelFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoPagination
