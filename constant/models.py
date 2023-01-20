from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

