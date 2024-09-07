from django.db import models

class TimeStampedModelMixin():
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)