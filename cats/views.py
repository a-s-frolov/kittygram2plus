from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle

from cats.models import Achievement, Cat, User
# from cats.pagination import CatsPagination
from cats.permissions import OwnerOrReadOnly  # , ReadOnly
from cats.serializers import (AchievementSerializer, CatSerializer,
                              UserSerializer)
from cats.throttling import WorkingHoursRateThrottle


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [OwnerOrReadOnly]
    throttle_classes = (
        AnonRateThrottle,
        ScopedRateThrottle,
        WorkingHoursRateThrottle
    )
    throttle_scope = 'low_request'
    pagination_class = None  # CatsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ('color', 'birth_year')
    search_fields = ('name',)
    ordering_fields = ('name', 'birth_year')

    '''def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''

    '''def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()'''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
