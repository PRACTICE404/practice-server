from rest_framework.serializers import ModelSerializer, HiddenField

from . import models


class SessionSerializer(ModelSerializer):

    class Meta:
        model = models.Session
        fields = "__all__"


class SessionSignalSerializer(ModelSerializer):

    class CurrentSessionDefault:
        requires_context = True

        def __call__(self, serializer_field):
            return models.Session.objects.filter(
                id=serializer_field.context['view'].kwargs.get('id', None)
            ).first()

    session = HiddenField(
        default=CurrentSessionDefault()
    )

    class Meta:
        model = models.SessionSignal
        fields = "__all__"
