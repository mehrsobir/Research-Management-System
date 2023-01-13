from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Institution(models.Model):
    name = models.CharField(max_length=255)
    founded_at = models.DateTimeField()
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
