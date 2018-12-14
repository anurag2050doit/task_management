from rest_framework.serializers import ModelSerializer, ReadOnlyField, CharField

from api.models import Task, Category, Tag


class TaskSerializers(ModelSerializer):
    assignee_name = ReadOnlyField(source='assigned_to.get_full_name')
    creator_name = ReadOnlyField(source='created_by.get_full_name')
    priority = CharField(source='get_priority_display')

    class Meta:
        model = Task
        fields = ('id', 'assignee_name', 'creator_name', 'title', 'priority')


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_deleted',)


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)
