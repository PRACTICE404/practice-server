from rest_framework.serializers import ModelSerializer

from . import models


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = models.Customer
        fields = '__all__'
