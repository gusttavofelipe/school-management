from django.db import models


class School(models.Model):
    name = models.CharField('Name', max_length=70)