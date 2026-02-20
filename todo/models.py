from django.db import models

# Create your models here.
class Todolist(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   status = models.BooleanField(default=False)
   
   def __str__(self):
      return f"{self.title} - {self.status}"

# model creation -> migration file create(makemigrations) -> db ma reflect(migrate)