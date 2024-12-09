from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models
from . import pagination


class SessionViewSet(ModelViewSet):
    permission_classes = []
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    ordering_fields = '__all__'


class SignalViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = serializers.SessionSignalSerializer
    queryset = models.SessionSignal.objects.all()
    pagination_class = pagination.SignalPagination


class SignalBySessionViewSet(SignalViewSet):
    queryset = None

    def get_queryset(self):
        return models.SessionSignal.objects.filter(session=self.kwargs.get('id', None))  # noqa
