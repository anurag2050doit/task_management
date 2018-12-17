from rest_framework import serializers

from api.models import Task, Category, Tag


class TaskListSerializers(serializers.ModelSerializer):
    assignee_name = serializers.ReadOnlyField(source='assigned_to.get_full_name')
    creator_name = serializers.ReadOnlyField(source='created_by.get_full_name')
    priority = serializers.CharField(source='get_priority_display')
    task_status = serializers.CharField(source='get_task_status_display')
    task_detail_link = serializers.HyperlinkedIdentityField(read_only=True, view_name='task-detail')
    assignee_user_link = serializers.HyperlinkedRelatedField(source='assigned_to', read_only=True,
                                                             view_name='user-detail')
    creator_user_link = serializers.HyperlinkedRelatedField(read_only=True, source='created_by',
                                                            view_name='user-detail')

    class Meta:
        model = Task
        fields = ('id', 'assignee_name', 'creator_name', 'priority', 'title', 'task_status', 'task_detail_link',
                  'assignee_user_link', 'creator_user_link')


class TaskDetailSerializers(serializers.ModelSerializer):
    assignee_name = serializers.ReadOnlyField(source='assigned_to.get_full_name')
    creator_name = serializers.ReadOnlyField(source='created_by.get_full_name')
    priority = serializers.CharField(source='get_priority_display')
    tag = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        exclude = ('is_deleted',)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_deleted',)


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)
