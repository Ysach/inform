import models
from rest_framework import serializers
from django.contrib.auth.models import User


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailUser
        # depth = 2
        fields = ('subject', 'email', 'content')


class EmailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailInfo
        fields = ('subject', 'email', 'content')


class MsgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MsgInfo
        fields = ('phone', 'msg')


class UserSerializer(serializers.ModelSerializer):
    # auth_users = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'auth_users')


class APIServerSerializer(serializers.ModelSerializer):
    # auth_users = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = models.APIServer
        fields = ('send_user', 'email_subject', 'to_email', 'email_content', 'phone_number', 'phone_content')
