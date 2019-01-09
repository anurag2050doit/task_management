from copy import deepcopy

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

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
        serializer = self.serializer_class(data=params, context={'request': request})
        serializer.initial_data['created_by'] = request.user.id
        if serializer.is_valid():
            task = serializer.save()
            try:
                tag_ids, category_ids = params.pop('tag'), params.pop('category')
                tags = [models.Tag.objects.get(id__exact=id) for id in tag_ids]
                [task.tag.add(tag) for tag in tags]
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                return Response({'error': 'Invalid Tags'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                categories = [models.Category.objects.get(id__exact=id) for id in category_ids]
                [task.category.add(category) for category in categories]
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                return Response({'error': 'Invalid Categories'})
            task.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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
