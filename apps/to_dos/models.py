from django.db import models
from abstracts.models import AbstractDateTime
from django.db.models import QuerySet

class Task(AbstractDateTime):
    MAX_LENGHT_TEXT = 255
    description = models.CharField(
        verbose_name = "Описание",
        null = False,
        max_length =  MAX_LENGHT_TEXT
    )

    todo = models.CharField(
        verbose_name = "Задание",
        null = False,
        max_length =  MAX_LENGHT_TEXT
    )

    is_active = models.BooleanField(
        verbose_name = "Aktivnost",
        default = True,
        null = False
    )

    def __str__(self) -> str:
        return f"Задание {self.id}:{self.todo}"
    
    class Meta:
        ordering = (
            'todo',
        )
        verbose_name = "Задание",
        verbose_name_plural = "Задание"
