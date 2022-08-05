from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import ProjectFilter
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer, \
    TodoModelCreateSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class TodoPagination(PageNumberPagination):
    page_size = 20


class ProjectModelFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class TodoModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.action == 'create':
            return TodoModelCreateSerializer
        return TodoModelSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]
