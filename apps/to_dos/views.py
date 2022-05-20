from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets  import ViewSet
from rest_framework.response  import Response as DRF_Responce
from rest_framework.request  import Request as DRF_Request

from django.db.models import QuerySet

from to_dos.models import Task
from to_dos.serializers import TaskSerializer

class TaskViewSet(ViewSet):
    
    permission_classes: 'typle' = (
        permissions.AllowAny,   
    )
    queryset: QuerySet[Task]= Task.objects.get_not_deleted()

    def get_queryset(self) -> QuerySet[CustomUser]:
        return self.queryset.filter(
            is_tusk=False
        )
    
    @actiion(
        methods=['post'],
        detail=False,
        url_path = 'task-endpoint',
        permissions_classes=(
            permissions.AllowAny
        )
    )

    def my_custom_endpoint(
        sels,
        request: DRF_Request
    ) -> DRF_Reponce:

        data: list = [
            tusk.id for user in self.get_queryset()
        ]
        return DRF_Responce(
            {'data': data}
        )
    def list(self, request: DRF_Responce) -> DRF_Responce:

        serializers: TaskSerializer = CustomUserSerializre(
            data=request.data
            )
        if serializer.is_valid():
            serializer.save()
            return DRF_Responce(
                {'data': 'Объект {serializer.id} создан'}
            )
        return DRF_Reponce(
            {'response': 'Объект не создан'}
        )
    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles GET-request with ID to show custom_user."""

        # Retrieving certain object
        #
        custom_user: Optional[Task] = None
        try:
            custom_user = self.get_queryset().get(
                id=pk
            )
        except Task.DoesNotExist:
            return DRF_Response( 
                {'response': 'Не нашел такого юзера'}
            )

        serializer: TaskSerializer = \
            TaskSerializer(
                custom_user
            )

        return DRF_Response(
            {'response': serializer.data}
        )       return DRF_Responce()



