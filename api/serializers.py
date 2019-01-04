from rest_framework import serializers

from api.models import Task, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_deleted',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)


class TaskSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=True)
    assignee_name = serializers.ReadOnlyField(source='assigned_to.get_full_name')
    creator_name = serializers.ReadOnlyField(source='created_by.get_full_name')
    priority_name = serializers.ReadOnlyField(source='get_priority_display')
    assignee_user_link = serializers.HyperlinkedRelatedField(source='assigned_to', read_only=True,
                                                             view_name='user-detail')
    creator_user_link = serializers.HyperlinkedRelatedField(read_only=True, source='created_by',
                                                            view_name='user-detail')

    class Meta:
        model = Task
        exclude = ('is_deleted',)
