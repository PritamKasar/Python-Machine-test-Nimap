from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    client = serializers.CharField(source="client.client_name", read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "project_name", "client", "users", "created_at", "created_by"]


class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ["project_name", "users"]
        
    def create(self, validated_data):
        users_data = validated_data.pop('users', [])
        user_ids = [u['id'] for u in users_data]  # extract IDs from nested dicts
        project = Project.objects.create(**validated_data)
        project.users.set(User.objects.filter(id__in=user_ids))
        return project
    
class ProjectListSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Client
        fields = ["id", "client_name", "created_at", "created_by"]


class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ["id", "client_name", "projects", "created_at", "created_by", "updated_at"]
