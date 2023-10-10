from django.db import models



class Serie(models.Model):
    name = models.CharField('Name', max_length=7)
    number_students = models.IntegerField('Number of students')
    shift = models.CharField('Shift', max_length=9)