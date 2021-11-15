from rest_framework.viewsets import GenericViewSet, mixins
from .models import User
from .serializers import UserSerializer


class UserCustomViewSet(mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
