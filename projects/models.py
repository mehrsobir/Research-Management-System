from django.db import models
from institutions.models import Department
from constant.models import Direction, Category, Status

class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лоиҳа'
        verbose_name_plural = 'Лоиҳаҳо'

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Мавзуъ'
        verbose_name_plural = 'Мавзуъҳо'

    def __str__(self):
        return self.name
