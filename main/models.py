from django.db import models
from users.models import Account
from constant.models import Category
from .validators import validate_file_extension

class Article(models.Model):
    name = models.CharField(max_length=255)
    annotation = models.TextField()
    pages = models.PositiveIntegerField()
    pub_date = models.DateField(null=True, blank=True)
    pub_place = models.CharField(max_length=255, null=True, blank=True)
    pub_link = models.CharField(max_length=255, null=True, blank=True)
    category  = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author  = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)
    pdf_file = models.FileField(upload_to='static/pdf/scientific', validators=[validate_file_extension], verbose_name='PDF-Файл', null=True, blank=True)

    class Meta:
        verbose_name = 'Мақола'
        verbose_name_plural = 'Мақолаҳо'

    def __str__(self):
        return self.name

class Article_pub(models.Model):
    name = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    pub_date = models.DateField(null=True, blank=True)
    pub_place = models.CharField(max_length=255, null=True, blank=True)
    pub_link = models.CharField(max_length=255, null=True, blank=True)
    category  = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author  = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)
    pdf_file = models.FileField(upload_to='static/pdf/public', validators=[validate_file_extension], verbose_name='PDF-Файл', null=True, blank=True)

    class Meta:
        verbose_name = 'Мақолаи оммавӣ'
        verbose_name_plural = 'Мақолаҳои оммавӣ'

    def __str__(self):
        return self.name

class TV(models.Model):
    topic = models.CharField(max_length=255)
    program_date = models.DateField()
    tv_name = models.CharField(max_length=255)
    tv_program = models.CharField(max_length=255, null=True, blank=True)
    program_link = models.CharField(max_length=255, null=True, blank=True)
    category  = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author  = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Барномаи телевизионӣ'
        verbose_name_plural = 'Барномаҳои телевизионӣ'

    def __str__(self):
        return self.topic

class Book(models.Model):
    name = models.CharField(max_length=255)
    annotation = models.TextField()
    pages = models.PositiveIntegerField()
    pub_date = models.DateField(null=True, blank=True)
    pub_place = models.CharField(max_length=255, null=True, blank=True)
    pub_link = models.CharField(max_length=255, null=True, blank=True)
    category  = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author  = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)
    pdf_file = models.FileField(upload_to='static/pdf/books', validators=[validate_file_extension], verbose_name='PDF-Файл', null=True, blank=True)

    class Meta:
        verbose_name = 'Китоб'
        verbose_name_plural = 'Китобҳо'

    def __str__(self):
        return self.name

class Radio(models.Model):
    topic = models.CharField(max_length=255)
    program_date = models.DateField()
    radio_name = models.CharField(max_length=255)
    radio_program = models.CharField(max_length=255, null=True, blank=True)
    program_link = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Барномаи радиоӣ'
        verbose_name_plural = 'Барномаҳои радиоӣ'

    def __str__(self):
        return self.topic

class Conference(models.Model):
    topic = models.CharField(max_length=255)
    conf_date = models.DateField()
    conf_name = models.CharField(max_length=255)
    conf_place = models.CharField(max_length=255)
    conf_link = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Конфронсу семинар'
        verbose_name_plural = 'Конфронсу семинарҳо'

    def __str__(self):
        return self.topic

