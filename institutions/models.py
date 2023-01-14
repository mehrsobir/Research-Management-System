from django.db import models
from users.models import Account
from constant.models import Education
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Institution(models.Model):
    name = models.CharField(max_length=255)
    founded_at = models.DateField()
    disabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Муассиса'
        verbose_name_plural = 'Муассисаҳо'

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    founded_at = models.DateField()
    disabled = models.BooleanField(default=False)
    head = models.OneToOneField(Account, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Шуъба'
        verbose_name_plural = 'Шуъбаҳо'

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=1)
    occupied = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    degree_needed = models.ForeignKey(Education, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вазифа'
        verbose_name_plural = 'Вазифаҳо'

    def __str__(self):
        return self.name
