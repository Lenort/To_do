from django.db import models

# Create your models here.
from datetime import datetime , timedelta

import uuid 

class AbstractDateTime(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Identification'
    )

    datetime_created = models.DateTimeField(
        verbose_name = 'Time Created',
        auto_now_add = True
    ) 

    datetime_deleted = models.DateTimeField(
        verbose_name = 'Time Deleted',
        null=True,
        blank=True,
        auto_now=True
    )

    datetime_live = models.DateTimeField(
        verbose_name = "Time",
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta:
        abstract = True