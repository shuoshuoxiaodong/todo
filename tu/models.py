from django.db import models
from datetime import date

# Create your models here.
class TODO(models.Model):
    thing = models.CharField(max_length=20, verbose_name='待办事项')
    done = models.BooleanField(default=False ,verbose_name='已完成')
    def _str_(self):
        return self.thing
    class Meta():
        db_table = 'tu'

class Student(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=10,null=False)
    apartment = models.TextField()
    birthday = models.DateField(default=date.today)
