from django.db import models
from institutions.models import Department
from constant.models import Direction, Category, Status
from users.models import Account

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
    taken = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Мавзуъ'
        verbose_name_plural = 'Мавзуъҳо'

    def __str__(self):
        return self.name



class Plan(models.Model):
    year = models.CharField(max_length=4, verbose_name='Сол')
    aproved = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Мавзуъ')
    print_list = models.DecimalField(max_digits=4, decimal_places=2, default=1,  verbose_name='Ҷузъи чопӣ')

    class Meta:
        verbose_name = 'Нақшаи инфродӣ'
        verbose_name_plural = 'Нақшаҳои инфродӣ'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + '-' + self.year

class Subtopic(models.Model):
    name = models.CharField(max_length=255)
    print_list = models.DecimalField(max_digits=4, decimal_places=2, default=1)
    due_date = models.DateField()
    excepted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    article_info = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('due_date',)
        verbose_name = 'Боб'
        verbose_name_plural = 'Бобҳо'

    def __str__(self):
        return self.name
