from rest_framework import serializers

from api.models import Task


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('id', 'is_deleted', 'created_at', 'modified_at')
