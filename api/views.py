from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from api import models
from api import serializers


# Create your views here.

class TasksAllAPI(ListAPIView):
    queryset = models.Task.objects.filter(is_deleted=False).exclude(task_status='CL')
    serializer_class = serializers.TaskListSerializers
    permission_classes = (AllowAny,)


class CategoriesAllAPI(ListAPIView):
    queryset = models.Category.objects.filter(is_deleted=False)
    serializer_class = serializers.CategorySerializers
    permission_classes = (AllowAny,)


class TagsAllAPI(ListAPIView):
    queryset = models.Tag.objects.filter(is_deleted=False)
    serializer_class = serializers.TagSerializers
    permission_classes = (AllowAny,)


class TaskSingleAPI(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = models.Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.TaskDetailSerializers
