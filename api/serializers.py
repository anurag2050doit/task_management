from rest_framework.serializers import ModelSerializer

from api.models import Task, Category, Tag


class TaskSerializers(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('is_deleted', 'created_at', 'modified_at')


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_deleted',)


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)
