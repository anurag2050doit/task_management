from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ('last_login', 'date_joined',)

    def create(self, validated_data):
        return User.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance
