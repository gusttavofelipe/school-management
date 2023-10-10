from django.db import models
from school.models import School
from serie.models import Serie


class Student(models.Model):
    name = models.CharField('Name', max_length=70)
    age = models.IntegerField('Age')
    school_uuid = models.ForeignKey(School, on_delete=models.CASCADE)
    serie_uuid = models.ForeignKey(Serie, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)