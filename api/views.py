from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from api import models
from api import serializers


# Create your views here.

class TaskAllAPI(ListAPIView):
    queryset = models.Task.objects.filter(is_deleted=False)
    serializer_class = serializers.TicketSerializers
    permission_classes = (AllowAny,)

