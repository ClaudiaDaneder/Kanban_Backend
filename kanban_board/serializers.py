from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, Board

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TaskListSerializer(serializers.ModelSerializer):
    project_lead = UserSerializer()
    created_by = UserSerializer()
    class Meta:
        model = Task
        fields = "__all__"

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'created_by': {'read_only': True}}

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project_lead', 'board', 'priority', 'deadline', 'status']
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        extra_kwargs = {'owner': {'read_only': True}}