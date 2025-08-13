from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Client, Project
from .serializers import (
    ClientSerializer, ClientDetailSerializer,
    ProjectSerializer, ProjectListSerializer
)

from django.contrib.auth import get_user_model

User = get_user_model()

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientDetailSerializer
        return ClientSerializer

    @action(detail=True, methods=['post'], url_path='projects')
    def create_project(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

        project_name = request.data.get('project_name')
        users_data = request.data.get('users', [])

        user_ids = [u['id'] for u in users_data if 'id' in u]

        try:
            default_user = User.objects.get(username=users_data[0]['name'])
        except User.DoesNotExist:
            return Response({"error": "Default user not found"}, status=status.HTTP_400_BAD_REQUEST)

        project = Project.objects.create(
            client=client,
            project_name=project_name,
            created_by=default_user
        )

        project.users.set(User.objects.filter(id__in=user_ids))

        response_data = {
            "id": project.id,
            "project_name": project.project_name,
            "client": client.client_name,
            "users": [{"id": u.id, "name": u.username} for u in project.users.all()],
            "created_at": project.created_at,
            "created_by": project.created_by.username
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    def get_queryset(self):
        user = self.request.user 
        model_fields = [f.name for f in Project._meta.fields]

        serializer_fields = [
            f for f in self.serializer_class().fields.keys() if f in model_fields
        ]

        queryset = Project.objects.all().values(*serializer_fields)

        for project in queryset:
            project['created_by'] = user.username if user.is_authenticated else None

        return queryset
