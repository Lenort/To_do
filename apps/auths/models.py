from django.db import models
from django.db.models import QuerySet


def get_not_deleted(self) -> QuerySet['Task']:
    return self.filter(
        datetime_deleted__isnull=True
    )

