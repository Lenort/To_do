from django.contrib import admin
from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from .models import (Task)
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_deleted',
        )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Task] = None) -> tuple:

        if not obj:
            return self.readonly_fields
            return self.readonly_fields + ('todo',)

admin.site.register(
    Task, TaskAdmin
)