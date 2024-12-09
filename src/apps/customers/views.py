from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class CustomerViewSet(ModelViewSet):
    permission_classes = []
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
