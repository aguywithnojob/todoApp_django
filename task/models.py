from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    time = models.DateField(auto_now_add=True)
    complete = models.BooleanField()


    def __str__(self):
        return self.task