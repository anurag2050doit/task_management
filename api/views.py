from copy import deepcopy

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api import models
from api import serializers


# Create your views here.


class TaskView(ModelViewSet):
    queryset = models.Task.objects.filter(is_deleted=False)
    serializer_class = serializers.TaskSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (AllowAny(),)
        return (IsAuthenticated(),)

    def create(self, request, *args, **kwargs):
        params = deepcopy(request.data)
        # tags = params.pop('tag')
        # categories = params.pop('category')
        serializer = self.serializer_class(data=params)
        serializer.initial_data['created_by'] = request.user.id
        if serializer.is_valid():
            task = serializer.save()
            # Add tag and categories to task
            # for tag in tags:
            #     tag_obj, is_created = models.Tag.objects.get_or_create(**tag)
            #     task.tag.add(tag_obj)
            # for cat in categories:
            #     cat_obj, is_created = models.Category.objects.get_or_create(**cat)
            #     task.category.add(cat_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagView(ModelViewSet):
    queryset = models.Tag.objects.filter(is_deleted=False)
    serializer_class = serializers.TagSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (AllowAny(),)
        return (IsAuthenticated(),)


class CategoryView(ModelViewSet):
    queryset = models.Category.objects.filter(is_deleted=False)
    serializer_class = serializers.CategorySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (AllowAny(),)
        return (IsAuthenticated(),)
